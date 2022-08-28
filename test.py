
import pandas as pd;
import numpy as np;
# arr = np.array([['maria', 'joao', 'andre'], [4, 5, 6]])
arr = [['maria', 'verde'], ['joao', 'azul'], ['paulo', 'amarelo'],['bruno', 'cinza']];
np.array_split(arr, 2);
df = pd.DataFrame(arr);
df=  df.rename({0:'nome', 1: 'cor'}, axis =1)

df.to_csv('C:/Users/Julia/teste.csv', sep=';', encoding='utf-8', index=False);