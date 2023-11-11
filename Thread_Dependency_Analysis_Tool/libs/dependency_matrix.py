from utils.transaction import Transaction


class DependencyMatrix:
    A: list[str] = []
    M: dict[dict[bool]] = {}
    size: int = 0

    def __init__(self, actions: list[str], transactions: dict[Transaction]):
        self.A = actions
        self.size = len(actions)
        for a1 in actions:
            self.M[a1] = {}
            for a2 in actions:
                self.M[a1][a2] = False

        for a1, t1 in transactions.items():
            for a2, t2 in transactions.items():
                mv1 = t1.getModifiedVariable()
                rvs1 = t1.getReadVariables()

                mv2 = t2.getModifiedVariable()
                rvs2 = t2.getReadVariables()

                if mv1 in rvs2 or mv2 in rvs1 or mv1 == mv2:
                    self.M[a1][a2] = True

    def printDependencyList(self):
        dp_list = []
        for a1 in self.A:
            for a2 in self.A:
                if self.M[a1][a2]:
                    dp_list.append("({}, {})".format(a1, a2))
        print("D = {" + ', '.join(dp_list) + "}")

    def printIndependencyList(self):
        idp_list = []
        for a1 in self.A:
            for a2 in self.A:
                if not self.M[a1][a2]:
                    idp_list.append("({}, {})".format(a1, a2))
        print("I = {" + ', '.join(idp_list) + "}")
