from ..modules.dependency_matrix import DependencyMatrix

import matplotlib.pyplot as plt
import igraph as ig
import numpy as np

# Try to uncomment if not working:
# import matplotlib
# matplotlib.use('TkAgg')


class DependencyGraph:
    def __init__(self, matrix: DependencyMatrix, w: str, labels_with_indices=False):
        self.labels_with_indices: bool = labels_with_indices
        self.FNF: list[list[str]]

        edges = []
        for i in range(len(w)):
            for j in range(i+1, len(w)):
                if matrix.M[w[i]][w[j]]:
                    edges.append((i, j))

        self.G: ig.Graph = ig.Graph(
            edges=edges,
            directed=True,
        )

        if labels_with_indices:
            self.G.vs['label'] = [a + ' [{}]'.format(str(i)) for i, a in enumerate(list(w))]
        else:
            self.G.vs['label'] = list(w)

    def remove_edge(self, source, target):
        eid = self.G.get_eid(source, target)
        self.G.delete_edges(eid)

    def transitive_reduction(self):
        V = self.G.vcount()

        adjacency = np.array(self.G.get_adjacency().data)
        closure = np.array(self.G.get_adjacency().data)

        for k in range(V):
            for i in range(V):
                for j in range(V):
                    closure[i, j] = closure[i, j] or (closure[i, k] and closure[k, j])

        closure_len_2_or_more = adjacency.dot(closure)

        for i in range(V):
            for j in range(V):
                if adjacency[i, j] and closure_len_2_or_more[i, j]:
                    self.remove_edge(i, j)

    def print_graph(self):
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

    def export_to_dot(self, directory_path: str):
        self.G.write(directory_path + 'graph.dot')

    def save_graph(self, directory_path: str):
        ig.plot(
            self.G,
            target=directory_path + 'plot.png',
            vertex_size=50,
            vertex_color='lightblue',
            edge_width=0.8,
            edge_color="gray",
            layout=self.G.layout("fr"),
            bbox=(800, 800),
            margin=100
        )

