#%%
import numpy as np
import pandas as pd
import build_grid
import scipy as sp
import build_network
import matplotlib.pyplot as plt
from sympy import Matrix
import networkx as nx

df_beijing = pd.read_pickle('..\\beijing_geolife_OD.pkl')
m = 40
n = 40
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
nwk.build_gragh(directed=True)
A = nwk.adjacency_matrix()
print(np.linalg.det(A))
# nwk.plot_vec(vec=counts, path_name=None, dictionary={val:i for i, val in enumerate(unique)})
dictionary={val:i for i, val in enumerate(unique)}
nwk.draw_network(counts = [counts[dictionary[i]] for i in nwk.G.nodes], save_path='G')
nwk.plot_degree_dist()
c = nwk.clustering_coefficient()
centrality = nwk.degree_centrality()
eigval, eigvec = np.linalg.eig(A)
plt.plot(abs(np.log((eigvec[0, :]))))
plt.show()
plt.close()

# %%

df_beijing['cell'] = cells
nodes = list(nwk.G.nodes)

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

hourly_count_vec = grid.create_vector(df_beijing, m*n, nodes, col_type='hourly')
daily_count_vec = grid.create_vector(df_beijing, m*n, nodes, col_type='daily')
normalized_hourly_count_vec = hourly_count_vec/hourly_count_vec.sum(axis=1, keepdims=True)

weekly_count_vec = grid.create_vector(df_beijing, m*n, nodes, col_type='weekly')
normalized_weekly_count = weekly_count_vec/weekly_count_vec.sum(axis = 1, keepdims = True)
# for i in range(col_size):
#     nwk.plot_vec(vec = count_vector[i], path_name= f's_{i}')

# %%

A = np.array(A)

plt.plot(normalized_hourly_count_vec[8],label='8 AM')
plt.plot(normalized_hourly_count_vec[18], label='6 PM')
plt.plot(normalized_hourly_count_vec[23], label='11 PM')
plt.xlabel('Node Idx')
plt.ylabel('Normalized Count')
plt.title('Hourly Traffic')
plt.legend()
plt.savefig('count_hour.png')
plt.close()

plt.plot(A@normalized_hourly_count_vec[8],label='8 AM')
plt.plot(A@normalized_hourly_count_vec[18], label='6 PM')
plt.plot(A@normalized_hourly_count_vec[23], label='11 PM')
plt.xlabel('Node Idx')
plt.ylabel('A*(Normalized Count)')
plt.title('Hourly Traffic')
plt.legend()
plt.savefig('A_count_hour.png')
plt.close()

# %%

N = A.shape[0]
C_line_shift = np.zeros((N, N))
C_line_shift[1:, :-1] = np.eye(N-1)
C_linear_bc = np.zeros((N, N))

char_poly = np.array(Matrix(A).charpoly().all_coeffs())[::-1]

C_linear_bc[:, -1] = -char_poly[:-1]

C = C_line_shift + C_linear_bc

adj = np.matrix(np.round(C, decimals=0), dtype=int)
comp_graph = nx.from_numpy_matrix(adj.T, create_using=nx.DiGraph())

labels = nx.get_edge_attributes(comp_graph,'weight')
nx.draw(comp_graph, pos=nx.circular_layout(comp_graph), with_labels=True, connectionstyle='arc3, rad = 0.1', node_size = 500, alpha = 0.6)
nx.draw_networkx_edge_labels(comp_graph, pos=nx.circular_layout(comp_graph), edge_labels=labels)
plt.savefig('C.png')
plt.close()
# %%

A = np.array(A)
weekly_count_vec = grid.create_vector(df_beijing, m*n, nodes, col_type='weekly')

weekday_counts = weekly_count_vec[:5].mean(axis = 0)
weekend_counts = weekly_count_vec[5:].mean(axis = 0)

weekday_counts = weekday_counts/weekday_counts.sum(keepdims=True)
weekend_counts = weekend_counts/weekend_counts.sum(keepdims=True)

plt.plot(weekday_counts, label='Weekdays')
plt.plot(weekend_counts, label='Weekend')
plt.xlabel('Node Idx')
plt.ylabel('Normalized Count')
plt.title('Weekly Traffic')
plt.legend()
plt.savefig('count_week.png')
plt.close()

plt.plot(A@weekday_counts, label='Weekdays')
plt.plot(A@weekend_counts, label='Weekend')
plt.xlabel('Node Idx')
plt.ylabel('A*(Normalized Count)')
plt.title('Weekly Traffic')
plt.legend()
plt.savefig('A_count_week.png')
plt.close()
# %%

weekly_count_vec = weekly_count_vec/weekly_count_vec.sum(axis = 1, keepdims = True)

for i in range(7):
    plt.plot(weekly_count_vec[i], label=week_days[i])

plt.xlabel('Node Idx')
plt.ylabel('Normalized Count')
plt.title('Daily Traffic')
plt.legend()
plt.savefig('count_daily.png')
plt.close()

#%% 

degree_sequence = sorted([(n, d) for n, d in nwk.G.degree()], reverse=True, key=lambda x: x[1])

node_with_high_deg = degree_sequence[0][0] # 693, 0 idx

plt.plot(hourly_count_vec[:, 0], '-*')
plt.title('Hourly Traffic')
plt.xlabel('Hour')
plt.xticks(range(24))
plt.ylabel('Count')
plt.savefig('hourly_traffic_interest.png')
plt.close()

plt.plot(weekly_count_vec[:, 0], '-*')
plt.title('Weekly Traffic')
plt.xticks(range(7), week_days)
plt.ylabel('Count')
plt.savefig('weekly_traffic_interest.png')
plt.close()

# %%

