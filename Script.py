import requests  # allows to send HTTP requests
import lxml  # processing XML and HTML
from bs4 import BeautifulSoup  # parsing HTML and XML docs
import csv  # writing in CSV files


def getHTMLcode():
    Searchinput = input("Enter the topic you want to search for :")
    Searchinput = Searchinput.replace(' ',
                                      '+')  # substiuting every space character in the user input in the search bar with '+' character
    link = "https://www.curlie.org/search?q=" + Searchinput + "&stime=92452189"  # adding the input after some processing to the curlie.org link
    Curliepage = requests.get(link)  # sends GET request for the URL
    HtmlText = Curliepage.content  # HTML code
    ParsedHtmlText = BeautifulSoup(HtmlText, "lxml")  # HTML code after organzing it in a way that can be read easily
    return ParsedHtmlText


def getData(ParsedHtmlText):
    links = []
    for link in ParsedHtmlText.findAll('div', attrs={
        'class': 'site-url'}):  # finding the div in the HTML code whose class name is 'site-url'
        l = link.text
        l = l.replace(' ', '')
        l = l.replace('\n', '')  # cleaning the link from other unwanted characters
        links.append(l)
    return links


def fileWrite(links):
    with open('links.csv', 'w', newline='') as csv_1:  # open csv file in write mode
        csv_out = csv.writer(csv_1)
        csv_out.writerows(
            [links[index]] for index in range(0, len(links)))  # write each element in the array list in a row


fileWrite(getData(getHTMLcode()))