import urllib.request
from bs4 import BeautifulSoup
import os

# Assigning link to a variable

myLink = "https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015"

# Opens the URL
getLink=urllib.request.urlopen(myLink)
f = open('game.txt', 'w+')
# Converts to HTML
soup = BeautifulSoup(getLink,  "html.parser")
# Prints Header for the wiki page
print(soup.h1.text)
for link in soup.findAll('div'):
    # Goes to the table and collects data from the class  wikitable sortable plainrowheaders
   table = soup.find("table", { "class" : "table table-bordered table-striped table-hover" })

# looping all elements in tr tags
for row in table.findAll('tr'):
    for h in row.findAll('th'):
        f.write(h.text+' ')
    for r in row.findAll('td'):
       cells = r.text
        # prints td elements
       print(cells)
       f.write(cells+'  ')
    f.write('\n')

       # elements = row.find('th')
        # prints th elements
        #print(elements.text)
f.close()