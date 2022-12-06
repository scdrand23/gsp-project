import data_preprocess
import build_grid
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
import scipy.sparse
import networkx as nx


a = [[1, 2], [2, 2]]
a_arr = sp.sparse.csr_matrix(a)
G = nx.from_scipy_sparse_matrix(a_arr, parallel_edges=True, create_using=nx.MultiGraph)
nx.draw(G)
plt.show()