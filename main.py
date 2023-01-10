import requests
from bs4 import BeautifulSoup

URL = "https://www.waalre.nl/inwoners-en-ondernemers/afvalstoffenheffing.html"

data = requests.get(URL,timeout=3).text
soup = BeautifulSoup(data,"html.parser")

print(soup.title.string)

for table in soup.find_all('table'):
    header = []
    rows = []
    for i,row in enumerate(table.find_all('tr')):
        if i == 0:
            header = [el.text.strip() for el in row.find_all('th')]
        else:
            rows.append([el.text.strip() for el in row.find_all('td')])
    print(header)
    for row in rows:
        print(row)
