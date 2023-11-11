from file_input_parser import FileInputParser
from dependency_matrix import DependencyMatrix
from dependency_graph import DependencyGraph
from fnf_determinator import FNFDeterminator

INPUT_DIRECTORY_PATH = "inputs/"
# INPUT_FILE_NAME = "test1"


def main():
    INPUT_FILE_NAME = input("Enter input filename: ")

    parser = FileInputParser()
    parser.read_input(INPUT_DIRECTORY_PATH + INPUT_FILE_NAME)
    parser.scan_and_parse()

    dependency_matrix = DependencyMatrix(parser.A, parser.T)
    dependency_matrix.printDependencyList()
    dependency_matrix.printIndependencyList()

    dependency_graph = DependencyGraph(dependency_matrix, parser.w)
    dependency_graph.transitive_reduction()

    fnf_determinator = FNFDeterminator(dependency_graph.G, parser.w)
    fnf_determinator.findFNF()
    fnf_determinator.printFNF()

    dependency_graph.exportToDot()
    dependency_graph.printGraph()
    dependency_graph.saveGraph()


if __name__ == "__main__":
    main()
