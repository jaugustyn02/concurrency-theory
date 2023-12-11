from lib.GaussianEliminationDependencyAnalysisTool.gedat import GEDAT
from modules.file_input_parser import FileInputParser
import concurrent.futures


class Task:
    def __init__(self, string: str):
        self.type = self.read_task_type(string)

        if self.type == 'A':
            self.i, self.k = self.read_A_indices(string)
        elif self.type == 'B':
            self.i, self.j, self.k = self.read_B_indices(string)
        elif self.type == 'C':
            self.i, self.j, self.k = self.read_C_indices(string)
        else:
            raise Exception('Invalid task type')
        
    def read_task_type(self, string: str):
        return string[0]
    
    def read_A_indices(self, A: str):
        return int(A[1])-1, int(A[3])-1
    
    def read_B_indices(self, B: str):
        return int(B[1])-1, int(B[3])-1, int(B[5])-1
    
    def read_C_indices(self, C: str):
        return int(C[1])-1, int(C[3])-1, int(C[5])-1


class CGE:
    def __init__(self, matrix: list[list[float]]):
        self.M = matrix
        self.M_size = len(matrix)
        self.gedat = GEDAT(self.M_size)
        self.fnf = self.gedat.get_fnf()

    
    # A_i_k - finding the multiplier for row i to subtract it from row k
    # m_k_i = M_k_i/M_i_i
    def thread_A(self, m: list[list[float]], M: list[list[float]], i: int, k: int):
        m[k][i] = M[k][i] / M[i][i]
    
    # B_i_j_k - multiplying the j-th element of row i by the multiplier to subtract from row k
    # n_k_i_j = M_i_j * m_k_i
    def thread_B(self, n: list[list[list[float]]], m: list[list[float]], M: list[list[float]], i: int, j: int, k: int):
        n[k][i][j] = M[i][j] * m[k][i]

    # C_i_j_k - subtracting the j-th element of row i from row k,
    # M_k_j = M_k_j - n_k_i
    def thread_C(self, M: list[list[float]], n: list[list[list[float]]], i: int, j: int, k: int):
        M[k][j] = M[k][j] - n[k][i][j]

    def read_A_indices(self, A: str):
        return int(A[1]), int(A[3])
    
    def print_2d_matrix(self, matrix: list[list[float]]):
        for row in matrix:
            for i, elem in enumerate(row):
                if i == len(row)-1:
                    print(f'| {elem:.2f}')
                else:
                    print(f'{elem:.2f}', end=' ')

    def print_3d_matrix(self, matrix: list[list[list[float]]]):
        for i, row in enumerate(matrix):
            print(f'k = {i}')
            for j, col in enumerate(row):
                for k, elem in enumerate(col):
                    if k == len(col)-1:
                        print(f'| {elem:.2f}')
                    else:
                        print(f'{elem:.2f}', end=' ')
            print()

    def run(self, verbose=False):
        print('Running CGE...')

        m = [[0 for _ in range(self.M_size)] for _ in range(self.M_size)]
        n = [[[0 for _ in range(self.M_size+1)] for _ in range(self.M_size)] for _ in range(self.M_size)]

        for section_id, section in enumerate(self.fnf):
            executor = concurrent.futures.ThreadPoolExecutor(max_workers=len(section))
            for task in section:
                task = Task(task)
                if task.type == 'A':
                    executor.submit(self.thread_A, m, self.M, task.i, task.k)
                elif task.type == 'B':
                    executor.submit(self.thread_B, n, m, self.M, task.i, task.j, task.k)
                elif task.type == 'C':
                    executor.submit(self.thread_C, self.M, n, task.i, task.j, task.k)
            executor.shutdown(wait=True)

            if verbose:
                print(f"Section: {section_id}")
                print("M: ")
                self.print_2d_matrix(self.M)
                print("m: ")
                self.print_2d_matrix(m)
                print("n: ")
                self.print_3d_matrix(n)
    
        print('Done!')
        print('Result:')
        self.print_2d_matrix(self.M)

    def save_matrix(self, file_name):
        with open(file_name, 'w') as f:
            for row in self.M:
                for i, elem in enumerate(row):
                    if i == len(row)-1:
                        f.write(f'{elem:.2f}\n')
                    else:
                        f.write(f'{elem:.2f} ')
    