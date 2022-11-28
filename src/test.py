import data_preprocess
import build_grid
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# df = pd.read_pickle('geolife.pkl')

# """
# beijing bounding box
# """
# # print(P[:5])
# grid = build_grid.bulid_grid_cells()
# # lat_min, lon_min,lat_max, lon_max = grid_bb.latInit, grid_bb.lonInit, grid_bb.latFinal, grid_bb.lonFinal
# # df_bejing = grid.coordinates_inside_beijing(df)
# # df_bejing.to_pickle('beijing_geolife.pkl')
# df_beijing = pd.read_pickle('beijing_geolife.pkl')
# print(len(df_beijing)/(len(df)))
df = data_preprocess.read_all_users('..\\Data')