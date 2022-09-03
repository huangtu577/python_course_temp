import numpy as np
import pandas as pd



N = 1e5


rng = np.random.default_rng()

x_data = pd.DataFrame(rng.normal(size=int(N)))

x_data[0].to_csv("Bar_Plots/testdata.csv", header=None, index=None)