import numpy as np
import pandas as pd
import glob
import os.path
import datetime
import os
import data_preprocess
import build_grid
# df = data_preprocess.read_all_users('..\\Data')
# df.to_pickle('beijing_geolife_OD.pkl')
# print(df.head())

df_beijing = pd.read_pickle('beijing_geolife_OD.pkl')
# print(df_beijing.head())
grid = build_grid.bulid_grid_cells()
xlat, xlon = grid.beijing_grid_cell_centers()


# print(xlat)

