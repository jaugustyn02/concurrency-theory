from collections import deque
import igraph as ig


class FNFDeterminator:
    def __init__(self, g: ig.Graph, w: str):
        self.G: ig.Graph = g
        self.w: str = w
        self.FNF_w: list[list[str]] = [[]]

    def findFNF(self):
        # Running BFS on graph G starting from every vertex, that does not have entering edges
        q = deque()
        section = [-1 for _ in range(self.G.vcount())]
        for vertex_index, degree in enumerate(self.G.degree(mode="in")):
            if degree == 0:
                q.append(vertex_index)
                section[vertex_index] = 0

        while len(q) > 0:
            vertex_index = q.popleft()
            for outgoing_vertex_index in self.G.neighbors(vertex_index, mode="out"):
                q.append(outgoing_vertex_index)
                section[outgoing_vertex_index] = section[vertex_index] + 1

        self.FNF_w: list[list[str]] = [[] for _ in range(max(section) + 1)]
        for vertex_index, s in enumerate(section):
            self.FNF_w[s].append(self.w[vertex_index])

    def printFNF(self):
        fnf_w = "FNF([w]) = "
        for section in self.FNF_w:
            fnf_w += '(' + "".join(sorted(section)) + ')'
        print(fnf_w)

    def saveFNF(self, directory_path: str):
        with open(directory_path + 'fnf.txt', 'w') as f:
            for section in self.FNF_w:
                f.write('(' + ",".join(sorted(section)) + ')')
