import requests
import lxml
from bs4 import BeautifulSoup
import csv

Searchinput = input("Enter the topic you want to search for :")
Searchinput = Searchinput.replace(' ', '+')
link = "https://www.curlie.org/search?q="+Searchinput+"&stime=92452189"
Curliepage = requests.get(link)

HtmlText = Curliepage.content
ParsedHtmlText = BeautifulSoup(HtmlText,"lxml")



links = []
for link in ParsedHtmlText.findAll('div', attrs={'class':'site-url'}):
    l = link.text
    l = l.replace(' ','')
    l = l.replace('\n','')
    links.append(l)


with open('links.csv', 'w', newline='') as csv_1:
  csv_out = csv.writer(csv_1)
  csv_out.writerows([links[index]] for index in range(0, len(links)))

