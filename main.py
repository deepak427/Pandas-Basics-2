import pandas as pd

from scipy import stats
import statistics

file_path = 'data/IBM-313 Marks.xlsx'

df = pd.read_excel(file_path)

x = df['Total']

print(stats.mode(x))

print(statistics.mode(x))


