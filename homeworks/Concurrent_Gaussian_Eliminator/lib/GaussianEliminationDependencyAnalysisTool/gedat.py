from lib.DependencyAnalysisTool.dat import DAT
from lib.DependencyAnalysisTool.config import Config as DATConfig
from lib.GaussianEliminationDependencyAnalysisTool.config import Config
from lib.GaussianEliminationDependencyAnalysisTool.modules.task import Task


# Gaussian Elimination Dependency Analysis Tool
class GEDAT:
    def __init__(self, matrix_size: int, cfg: Config = Config()):
        self.matrix_size = matrix_size
        self.build_alphabet()
        self.build_transactions()
        self.build_trace()
        
        dat_config = DATConfig(
            OUTPUT_DIRECTORY_PATH=cfg.OUTPUT_DIRECTORY_PATH,
            PRINT_FNF=cfg.PRINT_FNF,
            SAVE_FNF=cfg.SAVE_FNF,
            PRINT_PLOT=cfg.PRINT_PLOT,
            EXPORT_PLOT_TO_PNG=cfg.EXPORT_PLOT_TO_PNG,
            EXPORT_GRAPH_TO_DOT=cfg.EXPORT_GRAPH_TO_DOT,
            LABELS_WITH_INDICES=cfg.LABELS_WITH_INDICES
        )
        self.dat = DAT(self.alphabet,self.trace, self.transactions, dat_config)

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
