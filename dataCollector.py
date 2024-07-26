from bs4 import BeautifulSoup
import requests

def getPage(pageURL):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

    pageInfo = requests.get(pageURL, headers=headers)
    return pageInfo.text

def parsePage(htmlData):
    parse = BeautifulSoup(htmlData, 'html.parser')

    return parse

def getData(soup):
    stockTags = []
    table = soup.find('table', class_='cwl-symbols W(100%)')
    if table is None: #Doc: If table doesn't exist with that class_ or id
        print("ivan?")

    headers = [th.get_text(strip=True) for th in table.find_all('th')]

    for row in table.find_all('tr')[1:]:  
        cols = row.find_all('td')
        if len(cols) == len(headers):
            row_data = {headers[i]: cols[i].get_text(strip=True) for i in range(len(headers))}
            stockTags.append(row_data)
    
    return stockTags


htmlData = getPage('https://finance.yahoo.com/u/yahoo-finance/watchlists/most-active-penny-stocks/')
soup = parsePage(htmlData)
stockTags = getData(soup)






