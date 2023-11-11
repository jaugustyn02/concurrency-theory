class Transaction:
    modified_variable: str
    read_variables: list[str]

    def __init__(self, mv: str, rv: list[str]):
        self.modified_variable = mv
        self.read_variables = rv

    def getModifiedVariable(self) -> str:
        return self.modified_variable

    def getReadVariables(self) -> list[str]:
        return self.read_variables

    def __str__(self):
        return 'mv: {}, rv: {}'.format(self.modified_variable, self.read_variables)
