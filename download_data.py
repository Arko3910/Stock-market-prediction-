import requests

url = "https://query1.finance.yahoo.com/v7/finance/download/005930.KS?period1=0&period2=1893456000&interval=1d&events=history&includeAdjustedClose=true"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

response = requests.get(url, headers=headers)

with open("samsung_stock.csv", "wb") as f:
    f.write(response.content)
