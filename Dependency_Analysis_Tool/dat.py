from libs.file_input_parser import FileInputParser
from libs.dependency_matrix import DependencyMatrix
from libs.dependency_graph import DependencyGraph
from libs.fnf_determinator import FNFDeterminator
import config.config as conf

import sys


def main():
    if len(sys.argv) == 1:
        print(f"[USAGE]: {sys.argv[0].split('/')[-1]} <filename1> <filename2> ...")
        return

    for input_file_name in sys.argv[1:]:

        print(f"{input_file_name}:")

        parser = FileInputParser()
        parser.read_input(conf.INPUT_DIRECTORY_PATH + input_file_name)
        parser.scan_and_parse()

        dependency_matrix = DependencyMatrix(parser.A, parser.T)
        dependency_matrix.printDependencyList()
        dependency_matrix.printIndependencyList()

        dependency_graph = DependencyGraph(dependency_matrix, parser.w, conf.LABELS_WITH_INDICES)
        dependency_graph.transitive_reduction()

        fnf_determinator = FNFDeterminator(dependency_graph.G, parser.w)
        fnf_determinator.findFNF()
        if conf.PRINT_FNF:
            fnf_determinator.printFNF()

        if conf.PRINT_PLOT:
            dependency_graph.printGraph()
        if conf.EXPORT_PLOT_TO_PNG:
            dependency_graph.saveGraph(input_file_name)
        if conf.EXPORT_GRAPH_TO_DOT:
            dependency_graph.exportToDot(input_file_name)

        print()


if __name__ == "__main__":
    main()
