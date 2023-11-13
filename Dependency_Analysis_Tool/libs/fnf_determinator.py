from collections import deque
import igraph as ig


class FNFDeterminator:
    def __init__(self, g: ig.Graph, w: str):
        self.G: ig.Graph = g
        self.w: str = w
        self.FNF_w: list[list[str]] = [[]]

    def findFNF(self):
        q = deque()
        section = [-1 for _ in range(self.G.vcount())]
        for i, degree in enumerate(self.G.degree(mode="in")):
            if degree == 0:
                q.append(i)
                section[i] = 0

        while len(q) > 0:
            i = q.popleft()
            for j in self.G.neighbors(i, mode="out"):
                q.append(j)
                section[j] = section[i] + 1

        self.FNF_w: list[list[str]] = [[] for _ in range(max(section) + 1)]
        for i, s in enumerate(section):
            self.FNF_w[s].append(self.w[i])

    def printFNF(self):
        fnf_w = "FNF([w]) = "
        for s in self.FNF_w:
            fnf_w += '(' + "".join(sorted(s)) + ')'
        print(fnf_w)
