import numpy as np
import pandas as pd

dataset = pd.read_csv('forestfires.csv')

X = dataset.iloc[:, 0:12].values
y = dataset.iloc[:, 12].values