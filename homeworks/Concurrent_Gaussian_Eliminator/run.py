from cge import CGE
from modules.file_input_parser import FileInputParser
import os


def main():
    argv = os.sys.argv
    if len(argv) < 2:
        print(f'Usage: python {argv[0]} <input_file>')
        exit(1)
    input_file = argv[1]

    parser = FileInputParser(input_file)
    matrix = parser.get_matrix()
    cge = CGE(matrix)
    cge.run(verbose=False)
    cge.save_matrix('outputs/result.txt')


if __name__ == '__main__':
    main()