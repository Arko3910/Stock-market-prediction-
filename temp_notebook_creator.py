import nbformat
from nbformat.v4 import new_code_cell

nbook = nbformat.read('D:/Arko/Data sythesis project/stock_forecasting.ipynb', as_version=4)

for cell in nbook.cells:
    if 'https://query1.finance.yahoo.com/v7/finance/download/005930.KS?period1=0&period2=1893456000&interval=1d&events=history&includeAdjustedClose=true' in cell.source:
        cell.source = cell.source.replace('https://query1.finance.yahoo.com/v7/finance/download/005930.KS?period1=0&period2=1893456000&interval=1d&events=history&includeAdjustedClose=true', 'samsung_stock.csv')

nbformat.write(nbook, 'D:/Arko/Data sythesis project/stock_forecasting.ipynb')