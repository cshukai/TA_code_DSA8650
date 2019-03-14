import pandas as pd
import numpy as np
from plotnine import *


d=pd.read_csv("/dsa/data/all_datasets/USDA.csv")
usda_data=d[np.isfinite(d['Calories'])]
qplot("Calories", data=usda_data, geom="histogram",binwidth=10)
qplot(data=usda_data, x="Calories",  geom="histogram",weight = "Protein", binwidth=10)

ggplot(usda_data, aes(x="Calories")) + geom_histogram(binwidth=10, fill="lightblue") + ylab("Freqeuncy")
