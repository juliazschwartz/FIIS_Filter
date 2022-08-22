import requests as requests;
import pandas as pd;
from bs4 import BeautifulSoup;
import numpy as np;

webpage = requests.get('https://www.fundsexplorer.com.br/ranking');
result = webpage.text;
soup = BeautifulSoup(result, 'html.parser');
fiis = soup.find_all('tr');
resultados = [];
res = [];
for item in fiis:
    resultado = item.find_all('td');
    for f in resultado:
     res.append(f.text.strip());
     print(f.text.strip());


#     for fundo in resultado:
#       result = fundo.find_all('td');
#       for f in result:
#           resultados.append(f.text.strip());
# print(resultados);
   
# values = np.array([1,2]);
# values = np.array([str(v) for v in resultados]);

# df = pd.DataFrame(values);
# d = df.rename({0: 'codigo', 1: 'setor', 2:'preco_atual',
# 3: 'liquidez_diaria', 4:'dividendo',
# 5:'dividend_yield',6:'dy_3_meses_acumulado',7:'dy_6_meses_acumulado',8:'dy_12_meses_acumulado'
# ,9:'dy_3_meses_media',10:'dy_6_meses_media',11:'dy_12_meses_media',12:'dy_ano',13:'variacao_preco',14:'rentab_periodo'
# ,15:'rentab_acumulada',16:'patrimonio_liquido',17:'vpa',18:'p/vpa',19:'dy_patrimonial',20:'variacao_patrimonial'
# ,21:'rent_patrimonial_no_periodo',22:'rent_patrimonial_acumulada',23:'vacancia_fisica',24:'vacancia_financeira',25:'quantidade_ativos'

# }, axis='index')

# d.to_csv('C:/Users/Julia/fiis9.csv'); 