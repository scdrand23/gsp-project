import numpy as np
from scipy.spatial import KDTree

class bulid_grid_cells():
    def __init__(self, latInit = 39.4396, lonInit = 115.4238, latFinal = 41.06083, lonFinal = 117.50671, n=10, m=10):
        self.latInit = latInit
        self.lonInit = lonInit
        self.latFinal = latFinal
        self.lonFinal = lonFinal
        self.n = n
        self.m = m
        self.grid = self.create_2d_grid()
        self.lookup_tree = KDTree(self.grid)

    def beijing_grid_cell_centers(self):
        deltaLat = self.latFinal - self.latInit
        deltaLon = self.lonFinal - self.lonInit

        Xlat = np.linspace(self.latInit + deltaLat/(2*self.n), self.latFinal - deltaLat/(2*self.n), self.n) 
        Xlon = np.linspace(self.lonInit + deltaLon/(2*self.m), self.lonFinal - deltaLon/(2*self.m), self.m)

        return Xlat, Xlon

    def coordinates_inside_beijing(self, df):
        mask_in_beijing= (df['lon'] >= self.lonInit) & (df['lon'] <= self.lonFinal) & (df['lat'] >= self.latInit) & (df['lat'] <= self.latFinal)
        df_bejing = df[mask_in_beijing]
        return df_bejing

    def create_2d_grid(self):
        xlat, xlon = self.beijing_grid_cell_centers()
        x, y = np.meshgrid(xlat, xlon)
        return np.array((x.ravel(), y.ravel())).T

    def find_closest_cell(self, points):
        return self.lookup_tree.query(points)[1]

