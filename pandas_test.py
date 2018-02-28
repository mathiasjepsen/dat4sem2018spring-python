import pandas as pd
import numpy as np
filename = './befkbhalderstatkode.csv'

bef_stats_df = pd.read_csv(filename)
dd = bef_stats_df.as_matrix()

mask = (dd[:, 0] == 2015) & (dd[:, 3] == 5100) & (dd[:, 2] == 18)

print(np.sum(dd[mask][:, -1]))
