import numpy as np
import pandas as pd
class bulid_grid_cells():
    # def __init__(self) -> None:
    #     pass
    def __init__(self):
        self.latInit = 39.4396
        self.lonInit = 115.4238
        self.latFinal = 41.06083
        self.lonFinal = 117.50671
        # return self.latInit, self.lonInit, self.latFinal, self.lonFinal
    def beijing_grid_cell_centers(self):
        latInit = self.latInit
        lonInit = self.lonInit
        latFinal = self.latFinal
        lonFinal = self.lonFinal
        n = 28
        m = 36
        Xlat = np.zeros(n)
        Xlon = np.zeros(m)
        deltaLat = latFinal - latInit
        deltaLon = lonFinal - lonInit
        Xlat[0] = latInit + deltaLat/(2*n)
        Xlat[-1] = latFinal - deltaLat/(2*n)
        Xlon[0] = lonInit + deltaLon/(2*m)
        Xlon[-1] = lonFinal - deltaLon/(2*m)
        for i in range(1, len(Xlat)-1):
            Xlat[i] = Xlat[i-1]+deltaLat/n
            Xlon[i] = Xlon[i-1]+deltaLon/n
        return Xlat, Xlon

    def coordinates_inside_beijing(self, df):
        mask_in_beijing= (df['lon'] >= self.lonInit) & (df['lon'] <= self.lonFinal) & (df['lat'] >= self.latInit) & (df['lat'] <= self.latFinal)
        df_bejing = df[mask_in_beijing]
        return df_bejing
