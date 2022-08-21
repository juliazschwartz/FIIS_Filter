import requests as requests;
import pandas as pd;
from bs4 import BeautifulSoup;

webpage = requests.get('https://www.fundsexplorer.com.br/ranking');
result = webpage.text;
soup = BeautifulSoup(result, 'html.parser');
# print(soup.prettify());
# fiis = soup.find_all("div", {"class": "field field-name-field-select-state field-type-list-text field-label-above"});
# fiis = soup.find_all(id='table-ranking');
fiis = soup.find_all('tbody', class_= 'odd' );
print(fiis);  