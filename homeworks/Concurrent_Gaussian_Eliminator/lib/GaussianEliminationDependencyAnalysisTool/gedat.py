from lib.DependencyAnalysisTool.dat import DAT
from lib.DependencyAnalysisTool.config import Config as DATConfig
import lib.GaussianEliminationDependencyAnalysisTool.config as cfg
from lib.GaussianEliminationDependencyAnalysisTool.modules.task import Task


# Gaussian Elimination Dependency Analysis Tool
class GEDAT:
    def __init__(self, matrix_size: int):
        self.matrix_size = matrix_size
        self.build_alphabet()
        self.build_transactions()
        self.build_trace()
        
        dat_config = DATConfig(self.alphabet, self.trace, self.transactions, cfg.OUTPUT_DIRECTORY_PATH, cfg.LABELS_WITH_INDICES)
        self.dat = DAT(dat_config)

    def build_alphabet(self):
        self.alphabet = []
        for i in range(1, self.matrix_size + 1):
            for k in range(i+1, self.matrix_size + 1):
                self.alphabet.append(f'A{i}_{k}')
                for j in range(i, self.matrix_size + 2):
                    self.alphabet.append(f'B{i}_{j}_{k}')
                    self.alphabet.append(f'C{i}_{j}_{k}')

    def build_transactions(self):
        self.transactions = {}
        for i in range(1, self.matrix_size + 1):
            for k in range(i+1, self.matrix_size + 1):
                self.transactions[f'A{i}_{k}'] = f'm{k}_{i}=M{k}_{i}/M{i}_{i}'
                for j in range(i, self.matrix_size + 2):
                    self.transactions[f'B{i}_{j}_{k}'] = f'n{k}_{i}_{j}=m{k}_{i}*M{i}_{j}'
                    self.transactions[f'C{i}_{j}_{k}'] = f'M{k}_{j}=M{k}_{j}-n{k}_{i}_{j}'
        return self.transactions
    
    def build_trace(self):
        self.trace = ''.join(self.alphabet)

    def get_raw_fnf(self) -> list[list[str]]:
        return self.dat.get_fnf()

    def get_fnf(self) -> list[list[Task]]:
        raw_fnf = self.get_raw_fnf()
        fnf = []
        for section in raw_fnf:
            fnf_section = []
            for task in section:
                fnf_section.append(Task(task))
            fnf.append(fnf_section)
        return fnf


if __name__ == '__main__':
    cge = GEDAT(4)
    # cge.dat.print_fnf()
    # cge.dat.print_graph()
    cge.dat.save_graph_to_png()
    cge.dat.export_graph_to_dot()
    cge.dat.save_fnf()
    print(cge.get_fnf())
