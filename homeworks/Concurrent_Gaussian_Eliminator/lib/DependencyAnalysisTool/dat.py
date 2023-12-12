from .modules.input_parser import InputParser
from .modules.dependency_matrix import DependencyMatrix
from .modules.dependency_graph import DependencyGraph
from .modules.fnf_determinator import FNFDeterminator
from .config import Config


class DAT:
    def __init__(self, config: Config):
        self.config = config
        
        self.parser = InputParser(config.alphabet, config.raw_trace, config.raw_transactions)

        self.dependency_matrix = DependencyMatrix(self.parser.alphabet, self.parser.transactions)

        self.dependency_graph = DependencyGraph(self.dependency_matrix, self.parser.trace, config.labels_with_indices)
        self.dependency_graph.transitive_reduction()

        self.fnf_determinator = FNFDeterminator(self.dependency_graph.G, self.parser.trace)
        self.fnf_determinator.find_fnf()

    def printDependencyList(self):
        self.dependency_matrix.print_dependency_list()

    def printIndependencyList(self):
        self.dependency_matrix.print_independency_list()

    def print_fnf(self):
        self.fnf_determinator.print_fnf()

    def get_fnf(self):
        return self.fnf_determinator.get_fnf()

    def save_fnf(self):
        self.fnf_determinator.save_fnf(self.config.output_directory_path)

    def print_graph(self):
        self.dependency_graph.print_graph()

    def save_graph_to_png(self):
        self.dependency_graph.save_graph(self.config.output_directory_path)

    def export_graph_to_dot(self):
        self.dependency_graph.export_to_dot(self.config.output_directory_path)
