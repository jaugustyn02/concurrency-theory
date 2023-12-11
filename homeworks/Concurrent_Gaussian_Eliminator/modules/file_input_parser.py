

class FileInputParser:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None

    def open_file(self):
        try:
            self.file = open(self.file_name, 'r')
        except FileNotFoundError:
            print(f'[FileInputParser]: File {self.file_name} not found')
            exit(1)

    def close_file(self):
        if self.file is None:
            self.file.close()

    def parse_file_to_lines(self) -> list[str]:
        self.open_file()
        file_content = self.file.readlines()
        self.close_file()
        return file_content

    def get_matrix(self) -> list[list[float]]:
        file_lines = self.parse_file_to_lines()
        matrix_size = int(file_lines[0])
        matrix = [[0 for _ in range(matrix_size+1)] for _ in range(matrix_size)]
        for i in range(matrix_size):
            line = file_lines[i+1].split()
            for j in range(matrix_size):
                matrix[i][j] = float(line[j])
        y_col = file_lines[matrix_size+1].split()
        for i in range(matrix_size):
            matrix[i][matrix_size] = float(y_col[i])
        return matrix
