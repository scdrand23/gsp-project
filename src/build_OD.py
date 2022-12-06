# %%
import numpy as np
import pandas as pd
import build_grid
# df = data_preprocess.read_all_users('C:\\CMU\\18898_Graph\\Mobility_GSP\\Data')
# df.to_pickle('beijing_geolife_OD.pkl')

# %%
df_beijing = pd.read_pickle('..\\beijing_geolife_OD.pkl')

grid = build_grid.bulid_grid_cells(n=1000, m=1000)
cells = grid.find_closest_cell(df_beijing[['lat', 'lon']].to_numpy())
edges = []
for i in range(0, len(cells), 2):
    if cells[i] != cells[i+1]: # No self loops
        edges.append((cells[i], cells[i+1]))


# %%
