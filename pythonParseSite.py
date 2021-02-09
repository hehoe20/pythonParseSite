import requests
from bs4 import BeautifulSoup

site='https://www.skrivunder.net/signatures.php?tunnus=erkla&page_number=%PAGE%&num_rows=500'
allTables=''

r = requests.get(site.replace('%PAGE%','1'))
soup = BeautifulSoup(r.text, 'html.parser')
thead = soup.find("table", id="signatures").find('thead')
pages = soup.find('ul', {'class': 'pagination'})
soup = BeautifulSoup(str(pages), 'html.parser')
lastPage = soup.find_all('li')[-2].find('a').string

# the code above could have been used to fetch page one - but still we'll iterate from page one to lastpage

for x in range(1, int(lastPage)+1):
    #print the counting of every page fetched
    print(x)
    #replace page with counter x
    r = requests.get(site.replace('%PAGE%',str(x)))
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
with open("output.html", "w", encoding='utf-8') as file:
    #rewrite the table tag and thead and tbody tags
    file.write('<table>'+str(thead)+'<tbody>')
    file.write(allTables)
    file.write('</tbody></table>')
file.close()
