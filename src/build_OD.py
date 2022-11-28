# %%
import numpy as np
import pandas as pd
import glob
import os.path
import datetime
import os
import data_preprocess
import build_grid
# df = data_preprocess.read_all_users('C:\\CMU\\18898_Graph\\Mobility_GSP\\Data')
# df.to_pickle('beijing_geolife_OD.pkl')

# %%
df_beijing = pd.read_pickle('..\\beijing_geolife_OD.pkl')

grid = build_grid.bulid_grid_cells()
xlat, xlon = grid.beijing_grid_cell_centers()
x, y =np.meshgrid(xlat, xlon)
grid_lat_lon = np.array((x.ravel(), y.ravel())).T
cells = grid.find_closest_cell(grid_lat_lon, df_beijing[['lat', 'lon']].to_numpy())
edges = []
for i in range(0, len(cells), 2):
    if cells[i] != cells[i+1]: # No self loops
        edges.append((cells[i], cells[i+1]))


# %%
