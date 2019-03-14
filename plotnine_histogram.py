import pandas as pd
import numpy as np
import plotnine as p9

d=pd.read_csv("/dsa/data/all_datasets/USDA.csv")
usda_data=d[np.isfinite(d['Calories'])]
p9.qplot("Calories", data=usda_data, geom="histogram",binwidth=10)
