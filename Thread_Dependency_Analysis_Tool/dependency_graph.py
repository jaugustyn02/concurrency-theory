from dependency_matrix import DependencyMatrix
from copy import copy
import igraph as ig
import matplotlib
import matplotlib.pyplot as plt

# Uncomment if working on PyCharm:
# matplotlib.use('TkAgg')

OUTPUT_DIRECTORY_PATH = "outputs/"


class DependencyGraph:
    G: ig.Graph
    FNF: list[list[str]]
    label_with_index: bool

    def __init__(self, matrix: DependencyMatrix, w: str, label_with_index=False):
        self.label_with_index = label_with_index

        edges = []
        for i in range(len(w)):
            for j in range(i+1, len(w)):
                if matrix.M[w[i]][w[j]]:
                    edges.append((i, j))

        self.G = ig.Graph(
            edges=edges,
            directed=True,
        )

        if label_with_index:
            self.G.vs['label'] = [a + ' [{}]'.format(str(i)) for i, a in enumerate(list(w))]
        else:
            self.G.vs['label'] = list(w)

    def removeEdge(self, source, target):
        eid = self.G.get_eid(source, target)
        self.G.delete_edges(eid)

    def transitive_reduction(self):
        V = self.G.vcount()
        closure = copy(self.G.get_adjacency())
        to_delete = [[False for _ in range(V)] for _ in range(V)]

        for i in range(V):
            for j in range(V):
                for k in range(V):
                    if closure[i][j]:
                        to_delete[i][j] = to_delete[i][j] or (closure[i][k] and closure[k][j])

        for i in range(V):
            for j in range(V):
                if to_delete[i][j]:
                    self.removeEdge(i, j)

    def printGraph(self):
        fig, ax = plt.subplots()
        ig.plot(
            self.G,
            target=ax,
            vertex_size=50,
            vertex_color='lightblue',
            edge_width=0.8,
            edge_color="gray",
            layout=self.G.layout("fr"),
        )
        plt.show()

    def exportToDot(self):
        self.G.write(OUTPUT_DIRECTORY_PATH + 'graph.dot')

    def saveGraph(self):
        ig.plot(
            self.G,
            target=OUTPUT_DIRECTORY_PATH + 'plot.png',
            vertex_size=50,
            vertex_color='lightblue',
            edge_width=0.8,
            edge_color="gray",
            layout=self.G.layout("fr"),
            bbox=(800, 800),
            margin=100
        )

