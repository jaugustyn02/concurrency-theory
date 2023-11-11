from transaction import Transaction
import re


def extract_variables(expression):
    variable_names = re.findall(r'[a-zA-Z]+', expression)
    return variable_names


class FileInputParser:
    file_lines: list[str] = []
    A: list[str] = []
    w: str = ""
    T: dict[Transaction] = {}

    def __init__(self):
        pass

    def read_input(self, file_path: str):
        try:
            with open(file_path, 'r') as lines:
                for line in lines:
                    line = line.strip().replace(' ', '')
                    self.file_lines.append(line)
        except FileNotFoundError:
            print(f"FileNotFoundError: {file_path} file not found")
            exit()

    def scan_and_parse(self):
        if len(self.file_lines) < 3:
            return False
        # extract A
        self.A = self.file_lines[0].split('=')[1].split(',')
        # extract w
        self.w = self.file_lines[1].split('=')[1]
        # extract T
        for line in self.file_lines[2:]:
            action_name, transaction_str = line.split(':')
            transaction_str = transaction_str.split('=')

            read_variables = extract_variables(transaction_str[1])
            transaction = Transaction(transaction_str[0], read_variables)
            self.T[action_name] = transaction

        # for x, y in self.T.items():
        #     print(x, '-', y)
