import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import collections



class network_analysis():
    def __init__(self, edges) -> None:
       self.edges = edges

    def build_gragh(self, directed=False):
        if directed:
            self.G = nx.from_edgelist(self.edges, nx.DiGraph)
        else:
            self.G =  nx.from_edgelist(self.edges)
        return self.G

    def adjacency_matrix(self):
        return nx.to_numpy_matrix(self.G)
    
    def draw_network(self, counts, cmap='cool'):
        node_color = np.log(counts)
        nx.draw(self.G, cmap = cmap, node_color=node_color, with_labels=True)
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin = min(node_color), vmax=max(node_color)))
        sm._A = []
        plt.colorbar(sm)
        plt.show()

    def degree_dist(self):
        degree_sequence = sorted([d for n, d in self.G.degree()], reverse=True)  
        degreeCount = collections.Counter(degree_sequence)
        deg, cnt = zip(*degreeCount.items())
        return deg, cnt

    def plot_degree_dist(self):
        deg, cnt = self.degree_dist()
        plt.bar(deg, cnt, width=0.1)
        plt.show()

    def clustering_coefficient(self):
        n_edges = self.G.number_of_edges()
        n_nodes = len(self.G)
        c = (n_edges/4)*(((np.log(n_edges))**2)/n_nodes)
        return c
    
    def degree_centrality(self, type=''):
        if type == 'in':
            return nx.in_degree_centrality(self.G)
        elif type == 'out':
            return nx.out_degree_centrality(self.G)
        else:
            return nx.degree_centrality(self.G)
        