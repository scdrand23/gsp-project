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
    
    def draw_network(self, counts, cmap='cool', save_path=None):
        plt.rcParams["figure.figsize"] = (20,10)
        node_color = np.log(counts)
        nx.draw(self.G, cmap = cmap, node_color=node_color, node_size = len(self.G)//2, width = 0.5, with_labels=True, font_size=5)
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin = min(node_color), vmax=max(node_color)))
        sm._A = []
        plt.colorbar(sm)
        if save_path is not None:
            plt.savefig(save_path)
        else:
            plt.show()
        plt.close()
        plt.rcParams["figure.figsize"] = plt.rcParamsDefault["figure.figsize"]

    def degree_dist(self):
        degree_sequence = sorted([d for n, d in self.G.degree()], reverse=True)  
        degreeCount = collections.Counter(degree_sequence)
        deg, cnt = zip(*degreeCount.items())
        return deg, cnt

    def plot_degree_dist(self):
        deg, cnt = self.degree_dist()
        plt.bar(deg, cnt, width=0.1)
        plt.show()
        plt.close()

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

    def plot_vec(self, vec, path_name, dictionary):
        color_lookup = {i:abs(vec[dictionary[i]]) for i in self.G.nodes}
        low, *_, high = sorted(color_lookup.values())
        norm = plt.Normalize(vmin=low, vmax=high, clip=True)
        mapper = plt.cm.ScalarMappable(norm=norm, cmap=plt.cm.cool)
        plt.figure()  
        plt.colorbar(mapper, ax=plt.gca(), format='%.5f')
        nx.draw(self.G, 
                nodelist=color_lookup,
                node_size=500,
                node_color=[mapper.to_rgba(i) 
                        for i in color_lookup.values()], 
                with_labels=True)
        mapper._A = []
        plt.tight_layout()
        if path_name is not None:
            plt.savefig(path_name + '.png')
        else:
            plt.show()
        plt.close()
        