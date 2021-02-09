import requests
from bs4 import BeautifulSoup

#variables
site='https://www.skrivunder.net/signatures.php?tunnus=erkla&page_number=%PAGE%&num_rows=500'
filename='output.html'
allTables=''

#fetch first page from site above - look at url %PAGE% is replaced with 1
r = requests.get(site.replace('%PAGE%','1'))
soup = BeautifulSoup(r.text, 'html.parser')
lastPage = soup.find('ul', {'class': 'pagination'}).find_all('li')[-2].find('a').string
#store the table header for writing new header in table in output file
thead = soup.find("table", id="signatures").find('thead')
# the code fetches page 1 - but still we'll iterate from page one to lastpage
for pageNr in range(1, int(lastPage)+1):
    #print the counting of every page fetched
    print(pageNr)
    #replace page with counter x
    r = requests.get(site.replace('%PAGE%',str(pageNr)))
    #the following lines not needed for this ... but kept for other purposes
    headers = r.headers
    contentType = r.headers['content-type']
    encoding = r.encoding
    body = r.text
    #this is needed
    soup = BeautifulSoup(r.text, 'html.parser')
    #fetch the table with signatures and only get the table body
    tableWithSignatures=soup.find("table", id="signatures").find('tbody')
    #remove the tags for table body as we will join multiple tables into one
    tableWithSignatures=str(tableWithSignatures).replace('<tbody>','')
    tableWithSignatures=str(tableWithSignatures).replace('</tbody>','')
    #just the rows (and columns)
    allTables=allTables+str(tableWithSignatures)
#put everything into file
with open(filename, "w", encoding='utf-8') as file:
    #rewrite the table tag and thead and tbody tags
    file.write('<table>'+str(thead)+'<tbody>')
    file.write(allTables)
    file.write('</tbody></table>')
file.close()
