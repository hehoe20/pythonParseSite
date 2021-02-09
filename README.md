# pythonParseSite  <br />
This small python script extracts data from skrivunder.net - it takes the link (has to be defines within code) to a collection of signatures and iterates trough pages (range = last page is extracted from first page) with signatures and joins every table (removes table and thead tags) with signatures into a single html file (with only one table, thead and tbody tag).  <br />
Code could probably be optimized to do parsing even better.  <br />
Script requires beautifulsoup4 and requests:  <br />
pip install beautifulsoup4  <br />
pip install requests  <br />
