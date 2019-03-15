import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import diamonds
%matplotlib inline


p = ggplot(aes(x='carat', y='price'), diamonds)
p + geom_point(aes(color='carat'))


ggplot(aes(x = 'carat', y = 'price'),diamonds)+geom_point()+ geom_smooth(span=.3, se=False) + facet_wrap(['cut'])
