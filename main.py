import pandas as pd

from scipy import stats
import statistics

import numpy as np

file_path = 'data/IBM-313 Marks.xlsx'

df = pd.read_excel(file_path)

x = df['Total']

# finding mode of the column Total

print(stats.mode(x))

print(statistics.mode(x))

a = np.array([1,2,3,4,5])
print(np.percentile(a, 58))

def print_10_to_18():
    for i in range(10, 20, 2):
        if(i == 18):
            print(i)
        else:
            print(i, end=",")

print_10_to_18()

data = [1, 2, 4, 4, 463, 2, 3, 6, 8, 9, 4, 254, 6, 72]

def min_and_max(data):
    min_Val = min(data)
    max_val = max(data)
    return max_val-min_Val

print(min_and_max(data))




