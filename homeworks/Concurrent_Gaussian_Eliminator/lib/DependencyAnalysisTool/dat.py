from .modules.input_parser import InputParser
from .modules.dependency_matrix import DependencyMatrix
from .modules.dependency_graph import DependencyGraph
from .modules.fnf_determinator import FNFDeterminator
import threading
from .config import Config


class DAT:
    def __init__(self, alphabet, raw_trace, raw_transactions, config: Config):
        self.config = config
        
        self.parser = InputParser(alphabet, raw_trace, raw_transactions)

        self.dependency_matrix = DependencyMatrix(self.parser.alphabet, self.parser.transactions)

        self.dependency_graph = DependencyGraph(self.dependency_matrix, self.parser.trace, config.LABELS_WITH_INDICES)
        self.dependency_graph.transitive_reduction()

        self.fnf_determinator = FNFDeterminator(self.dependency_graph.G, self.parser.trace)
        self.fnf_determinator.find_fnf()

        if config.PRINT_FNF:
            self.print_fnf()
        
        if config.SAVE_FNF:
            self.save_fnf()

        if config.PRINT_PLOT:
            self.print_graph()
        
        if config.EXPORT_PLOT_TO_PNG:
            self.save_graph_to_png()

        if config.EXPORT_GRAPH_TO_DOT:
            self.export_graph_to_dot()

    def printDependencyList(self):
        self.dependency_matrix.print_dependency_list()

    def printIndependencyList(self):
        self.dependency_matrix.print_independency_list()

    def print_fnf(self):
        self.fnf_determinator.print_fnf()

    def get_fnf(self):
        return self.fnf_determinator.get_fnf()

    def save_fnf(self):
        self.fnf_determinator.save_fnf(self.config.OUTPUT_DIRECTORY_PATH)

    def print_graph(self):
        graph_thread = threading.Thread(target=self.dependency_graph.print_graph)
        graph_thread.start()
        # self.dependency_graph.print_graph()

    def save_graph_to_png(self):
        self.dependency_graph.save_graph(self.config.OUTPUT_DIRECTORY_PATH)

    def export_graph_to_dot(self):
        self.dependency_graph.export_to_dot(self.config.OUTPUT_DIRECTORY_PATH)
