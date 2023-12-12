class Transaction:
    modified_variable: str
    read_variables: list[str]

    def __init__(self, mv: str, rv: list[str]):
        self.modified_variable = mv
        self.read_variables = rv

    def get_modified_variable(self) -> str:
        return self.modified_variable

    def get_read_variables(self) -> list[str]:
        return self.read_variables

    def __str__(self):
        return 'mv: {}, rv: {}'.format(self.modified_variable, self.read_variables)
