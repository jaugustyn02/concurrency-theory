from lib.Dependency_Analysis_Tool.dat import DAT
from lib.Dependency_Analysis_Tool.config import Config as DATConfig


# Gaussian Elimination Dependency Analysis Tool
class GEDAT:
    def __init__(self, matrix_size: int):
        self.matrix_size = matrix_size
        self.build_alphabet()
        self.build_transactions()
        self.build_trace()
        
        dat_config = DATConfig(self.alphabet, self.trace, self.transactions, "outputs/", False)
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


if __name__ == '__main__':
    cge = GEDAT(3)
    # cge.dat.printFNF()
    # cge.dat.printGraph()
    cge.dat.saveGraphToPNG()
    cge.dat.exportGraphToDot()
    cge.dat.saveFNF()
