from ..modules.transaction import Transaction
import re



# ACTION_SYMBOL_PATTERN = r'[A-Z]([0-9]+(_[0-9]+)*|[0-9]*)'
ACTION_SYMBOL_PATTERN = r'[A-Z](?:[0-9]+(?:_[0-9]+)*|[0-9]*)'
VARIABLE_NAME_PATTERN = r'[a-zA-Z](?:[0-9]+(?:_[0-9]+)*|[0-9]*)'
DEFINED_TRANSACTION_PATTERN = r'^('+VARIABLE_NAME_PATTERN+'=.+)?$'


def extract_variables(expression):
    variable_names = re.findall(VARIABLE_NAME_PATTERN, expression)
    return variable_names


def extract_action_symbols(expression):
    action_symbols = re.findall(ACTION_SYMBOL_PATTERN, expression)
    return action_symbols


def expression_is_valid(expression, pattern) -> bool:
    return re.fullmatch(pattern, expression) is not None


class InputParser:
    def __init__(self, alphabet: list[str], raw_trace: str, raw_transactions: dict[str, str]):
        self.alphabet: list[str] = alphabet
        self.validate_alphabet()
        self.trace: list[str]
        self.parse_trace(raw_trace)
        self.transactions: dict[str, Transaction]
        self.parse_transactions(raw_transactions)
        
    
    def validate_alphabet(self):
        try:
            for symbol in self.alphabet:
                if not expression_is_valid(symbol, ACTION_SYMBOL_PATTERN):
                    raise ValueError(f"Invalid action symbol in alphabet: {symbol}")
        except ValueError as e:
            print("[ValidateAlphabet] InvalidInputError:", str(e))
            exit()


    def parse_trace(self, raw_trace: str):
        try:
            extracted_symbols = extract_action_symbols(raw_trace)
            for symbol in extracted_symbols:
                if symbol not in self.alphabet:
                    raise ValueError(f"Invalid action symbol in trace: {symbol}" +
                                     f"\nAction symbols must belong to the alphabet = {{{','.join(self.alphabet)}}}")
            self.trace = extracted_symbols
            
        except ValueError as e:
            print("[ParseTrace] InvalidInputError:", str(e))
            exit()
            
            
    def parse_transactions(self, raw_transactions: dict[str, str]):
        try:
            self.transactions = {}
            for i, (action_symbol, transaction_str) in enumerate(raw_transactions.items()):
                if transaction_str is None or transaction_str == {}:
                    self.transactions[action_symbol] = Transaction('', [])
                    continue
                if not expression_is_valid(transaction_str, DEFINED_TRANSACTION_PATTERN):
                    raise ValueError(f"Invalid definition of transaction {i}: {action_symbol}: {transaction_str}")

                if action_symbol not in self.alphabet:
                    raise ValueError(f"Invalid action symbol in transaction {i}: {action_symbol}" +
                                     f"\nAction symbols must belong to the alphabet = {{{','.join(self.alphabet)}}}")

                transaction_str_split = transaction_str.split('=')
                read_variables = extract_variables(transaction_str_split[1])
                transaction_str = Transaction(transaction_str_split[0], read_variables)
                self.transactions[action_symbol] = transaction_str

            for action_symbol in self.alphabet:
                if self.transactions.get(action_symbol) is None:
                    self.transactions[action_symbol] = Transaction('', [])
                    
        except ValueError as e:
            print("[ParseTransactions] InvalidInputError:", str(e))
            exit()
