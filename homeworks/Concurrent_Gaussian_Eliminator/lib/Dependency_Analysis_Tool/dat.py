# from .modules.file_input_parser import FileInputParser
from .modules.input_parser import InputParser
from .modules.dependency_matrix import DependencyMatrix
from .modules.dependency_graph import DependencyGraph
from .modules.fnf_determinator import FNFDeterminator
from .config import Config


class DAT:
    def __init__(self, config: Config):
        self.config = config

        # self.parser = FileInputParser()
        # self.parser.read_input(self.filepath)
        # self.parser.scan_and_parse()
        
        self.parser = InputParser(config.alphabet, config.raw_trace, config.raw_transactions)

        self.dependency_matrix = DependencyMatrix(self.parser.alphabet, self.parser.transactions)
        # self.dependency_matrix.printDependencyList()
        # self.dependency_matrix.printIndependencyList()

        self.dependency_graph = DependencyGraph(self.dependency_matrix, self.parser.trace, False)
        self.dependency_graph.transitive_reduction()

        self.fnf_determinator = FNFDeterminator(self.dependency_graph.G, self.parser.trace)
        self.fnf_determinator.findFNF()

    def printFNF(self):
        self.fnf_determinator.printFNF()

    def printGraph(self):
        self.dependency_graph.printGraph()

    def saveGraphToPNG(self):
        self.dependency_graph.saveGraph(self.config.output_directory_path)

    def exportGraphToDot(self):
        self.dependency_graph.exportToDot(self.config.output_directory_path)
