from lib.GaussianEliminationDependencyAnalysisTool.gedat import GEDAT
from modules.file_input_parser import FileInputParser
from modules.matrix_helper import MatrixHelper as mh
from config import Config
from lib.GaussianEliminationDependencyAnalysisTool.config import Config as gedatConfig
import concurrent.futures


# Concurrent Gaussian Elimination
class CGE:
    def __init__(self, matrix: list[list[float]], cnf: Config = Config()):
        self.M = matrix
        self.M_size = len(matrix)
        self.cnf = cnf

        self.gedatConfig = gedatConfig(
            OUTPUT_DIRECTORY_PATH=cnf.OUTPUT_DIRECTORY_PATH,
            PRINT_FNF=cnf.PRINT_FNF,
            SAVE_FNF=cnf.SAVE_FNF,
            PRINT_PLOT=cnf.PRINT_PLOT,
            EXPORT_PLOT_TO_PNG=cnf.EXPORT_PLOT_TO_PNG,
            EXPORT_GRAPH_TO_DOT=cnf.EXPORT_GRAPH_TO_DOT,
        )

    # A_i_k - finding the multiplier for row i to subtract it from row k,
    # m_k_i = M_k_i/M_i_i
    def thread_A(self, m: list[list[float]], M: list[list[float]], i: int, k: int):
        m[k][i] = M[k][i] / M[i][i]
    
    # B_i_j_k - multiplying the j-th element of row i by the multiplier to subtract from row k,
    # n_k_j = M_i_j * m_k_i
    def thread_B(self, n: list[list[list[float]]], m: list[list[float]], M: list[list[float]], i: int, j: int, k: int):
        n[k][j] = M[i][j] * m[k][i]

    # C_i_j_k - subtracting the j-th element of row i from row k,
    # M_k_j = M_k_j - n_k_i
    def thread_C(self, M: list[list[float]], n: list[list[list[float]]], _i: int, j: int, k: int):
        M[k][j] = M[k][j] - n[k][j]

    def choose_pivot(self, M: list[list[float]], i: int):
        for row in range(i, self.M_size):
            if M[row][i] != 0:
                return row
        return -1
    
    def switch_rows(self, M: list[list[float]], i: int, j: int):
        M[i], M[j] = M[j], M[i]
    
    def run(self):
        if self.cnf.VERBOSE:
            print('Running GEDAT...')

        self.gedat = GEDAT(self.M_size, self.gedatConfig)
        self.fnf = self.gedat.get_fnf()

        if self.cnf.VERBOSE:
            print('Done! - FNF generated')
            print('Running CGE...\n')

        m = [[0 for _ in range(self.M_size)] for _ in range(self.M_size)]
        n = [[0 for _ in range(self.M_size+1)] for _ in range(self.M_size)]

        # Variable to track column that is currently being reduced
        curr_col_to_reduce = 0

        for section_id, section in enumerate(self.fnf):
            executor = concurrent.futures.ThreadPoolExecutor(max_workers=len(section))
            for task in section:
                if task.type == 'A':
                    if task.i == curr_col_to_reduce and task.k == curr_col_to_reduce+1:
                        pivot_row = self.choose_pivot(self.M, curr_col_to_reduce)
                        if pivot_row == -1:
                            print("Error: Matrix is singular!")
                            exit(1)
                        if pivot_row != curr_col_to_reduce:
                            self.switch_rows(self.M, curr_col_to_reduce, pivot_row)
                        curr_col_to_reduce += 1
                    executor.submit(self.thread_A, m, self.M, task.i, task.k)
                elif task.type == 'B':
                    executor.submit(self.thread_B, n, m, self.M, task.i, task.j, task.k)
                elif task.type == 'C':
                    executor.submit(self.thread_C, self.M, n, task.i, task.j, task.k)
            executor.shutdown(wait=True)

            if self.cnf.VERBOSE:
                print(f"Section: {section_id}")
                print("M: ")
                mh.print_2d_matrix(self.M)
                print("m: ")
                mh.print_2d_matrix(m)
                print("n: ")
                mh.print_2d_matrix(n)
                print()
    
        if self.cnf.VERBOSE:
            print('Matrix reduced to row echelon form')
            mh.print_2d_matrix(self.M)

        # Divide each row by the leading coefficient
        for row in range(self.M_size):
            self.M[row] = [self.M[row][col]/self.M[row][row] for col in range(self.M_size+1)]

        if self.cnf.VERBOSE:
            print('Matrix divided by leading coefficients')
            mh.print_2d_matrix(self.M)

        # Back substitution
        for col in range(self.M_size-1, -1, -1):
            for row in range(col-1, -1, -1):
                self.M[row][self.M_size] -= self.M[row][col] * self.M[col][self.M_size]
                self.M[row][col] = 0

        # Fixing minus zeros floating point errors (-0.0 -> 0.0)
        for row in range(self.M_size):
            for col in range(self.M_size+1):
                self.M[row][col] += 0.0
            
        if self.cnf.PRINT_RESULT_MATRIX:
            if self.cnf.VERBOSE: print()
            print('Result matrix:')
            mh.print_2d_matrix(self.M)

        if self.cnf.SAVE_RESULT_MATRIX:
            mh.save_matrix(self.M, self.cnf.OUTPUT_DIRECTORY_PATH+'result.txt')
            if self.cnf.VERBOSE: print(f'Result matrix saved to {self.cnf.OUTPUT_DIRECTORY_PATH}result.txt')
