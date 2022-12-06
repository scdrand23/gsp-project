
import numpy as np
import pandas as pd
import build_grid
import scipy as sp
import build_network
import matplotlib.pyplot as plt

df_beijing = pd.read_pickle('C:\\Users\\Derej C Shenkut\\Documents\\PHD\\F22\\GSP&GL\\Project\\Data\\beijing_geolife_OD.pkl')
m = 5
n = 5
grid = build_grid.bulid_grid_cells(n=n, m=m)
cells = grid.find_closest_cell(df_beijing[['lat', 'lon']].to_numpy())
unique, counts = np.unique(cells, return_counts=True)
s = np.zeros((m*n))
s[unique] = counts
edges = []
for i in range(0, len(cells), 2):
    if cells[i] != cells[i+1]: 
        edges.append((cells[i], cells[i+1]))

nwk = build_network.network_analysis(edges)
nwk.build_gragh()
A = nwk.adjacency_matrix()
nwk.draw_network(counts= counts)
nwk.plot_degree_dist()
c = nwk.clustering_coefficient()
centrality = nwk.degree_centrality()
eigval, eigvec = np.linalg.eig(A)
plt.plot(abs(np.log((eigvec[0, :]))))
plt.show()

