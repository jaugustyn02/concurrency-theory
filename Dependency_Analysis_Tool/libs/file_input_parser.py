from utils.transaction import Transaction
import re


ALPHABET_PATTERN = r'^A=[a-zA-Z](,[a-zA-Z])*$'
WORD_PATTERN = r'^w=[a-zA-Z]+$'
DEFINED_TRANSACTION_PATTERN = r'^[a-zA-Z]:([a-z][0-9]?=.+)?$'
EMPTY_TRANSACTION_PATTERN = r'^[a-zA-Z]:$'
VARIABLE_NAME_PATTERN = r'[a-z][0-9]?'


def extract_variables(expression):
    variable_names = re.findall(VARIABLE_NAME_PATTERN, expression)
    return variable_names


def expression_is_valid(expression, pattern) -> bool:
    return re.fullmatch(pattern, expression) is not None


class FileInputParser:
    def __init__(self):
        self.file_lines: list[str] = []
        self.A: list[str] = []
        self.w: str = ""
        self.T: dict[str, Transaction] = {}

    def read_input(self, file_path: str):
        try:
            with open(file_path, 'r') as lines:
                for line in lines:
                    line = line.strip().replace(' ', '')
                    self.file_lines.append(line)
        except FileNotFoundError:
            print(f"[FileNotFoundError]: '{file_path}' file or directory not found")
            exit()

    def scan_and_parse(self):
        try:
            if len(self.file_lines) < 2:
                raise ValueError("Alphabet A and word w definitions are missing")

            # Extracting A with validation
            if not expression_is_valid(self.file_lines[0], ALPHABET_PATTERN):
                raise ValueError("Invalid syntax in line 1: " + self.file_lines[0] +
                                 "\nLine 1 must follow pattern: 'A=a | A=a, b, c ...' where a, b and c are action "
                                 "symbols, that must be a single lowercase or uppercase letter of the English "
                                 "alphabet)" +
                                 "\nFor example: A = a, b, c, d")

            self.A = self.file_lines[0].split('=')[1].split(',')

            # Extracting w with validation
            if not expression_is_valid(self.file_lines[1], WORD_PATTERN):
                raise ValueError("Invalid syntax in line 2: " + self.file_lines[1])

            self.w = self.file_lines[1].split('=')[1]

            # Checking if every symbol in w belongs to alphabet A
            for c in self.w:
                if c not in self.A:
                    raise ValueError(f"Invalid action symbol in word w: {c}" +
                                     f"\nAction symbols must belong to the alphabet A = {{{','.join(self.A)}}}")

            # Extracting T with validation
            for i in range(2, len(self.file_lines)):
                line = self.file_lines[i]
                if line == "":
                    continue
                if expression_is_valid(line, EMPTY_TRANSACTION_PATTERN):
                    action = line[:-1]
                    self.T[action] = Transaction('', [])
                    continue
                if not expression_is_valid(self.file_lines[i], DEFINED_TRANSACTION_PATTERN):
                    raise ValueError(f"Invalid definition of transaction in line {i+1}: {line}" +
                                     f"\nThis line must follow pattern: 'a: | a: x=2y + z1 ...' where a must belong to "
                                     f"alphabet A = {{{','.join(self.A)}}}" +
                                     "\nFor example: a: x = x + 2y")

                line_split = line.split(':')
                action, transaction_str = line_split

                # Checking if action symbol belongs to the Alphabet A
                if action not in self.A:
                    raise ValueError(f"Invalid action symbol in line {i+1}: {action}" +
                                     f"\nAction symbols must belong to the alphabet A = {{{','.join(self.A)}}}")

                transaction_str_split = transaction_str.split('=')
                read_variables = extract_variables(transaction_str_split[1])
                transaction = Transaction(transaction_str_split[0], read_variables)
                self.T[action] = transaction

            # Checking if every action in Alphabet A was defined
            for action in self.A:
                if self.T.get(action) is None:
                    self.T[action] = Transaction('', [])

        except ValueError as e:
            print("[InvalidInputError]: ", str(e))
            exit()

