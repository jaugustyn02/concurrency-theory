from cge import CGE
from config import Config
from modules.file_input_parser import FileInputParser
import os


def main():
    argv = os.sys.argv
    if len(argv) < 2:
        print(f'Usage: python {argv[0]} <input_file>')
        exit(1)

    input_file = argv[1]
    
    if not os.path.isfile(input_file):
        print(f'Error: file not found: {input_file}')
        exit(1)

    parser = FileInputParser(input_file)
    matrix = parser.get_matrix()

    cge = CGE(matrix)
    cge.run()


if __name__ == '__main__':
    main()