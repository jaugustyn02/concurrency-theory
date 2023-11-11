from libs.file_input_parser import FileInputParser
from libs.dependency_matrix import DependencyMatrix
from libs.dependency_graph import DependencyGraph
from libs.fnf_determinator import FNFDeterminator
from setup.setup import INPUT_DIRECTORY_PATH


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

    dependency_graph.printGraph()
    dependency_graph.exportToDot(INPUT_FILE_NAME)
    dependency_graph.saveGraph(INPUT_FILE_NAME)


if __name__ == "__main__":
    main()
