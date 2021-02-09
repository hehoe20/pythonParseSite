import requests
from bs4 import BeautifulSoup

allTables=''

for x in range(1, 80):
    print(x)
    r = requests.get('https://www.skrivunder.net/signatures.php?tunnus=erkla&page_number='+str(x)+'&num_rows=500')
    headers = r.headers['content-type']
    encoding = r.encoding
    body = r.text
    soup = BeautifulSoup(body, 'html.parser')
    tableWithSignatures=soup.find("table", id="signatures")
    allTables=allTables+str(tableWithSignatures)
with open("output.html", "w", encoding='utf-8') as file:
    file.write(allTables)
file.close()

