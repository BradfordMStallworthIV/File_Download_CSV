#Senior Project
#Brad Stallworth
#Automate csv downloads

from bs4 import BeautifulSoup as bs #will be used to navigate the messy HTML behind the webpage
import requests #will be used to talk to the web page. 
import wget #will be used to download the hyperlinks in the web page.


URL = 'https://support.spatialkey.com/spatialkey-sample-csv-data/' #Insert the URL of the webpage here that you wish to download from.
FILETYPE = '.csv' #Insert the File type here. Examples of file types: word(.docx) excel(xlsx, csv) text files (.txt) images(.jpeg)

def get_soup(url):
    return bs(requests.get(url).text, 'html.parser') #BeautifulSoup is  used to turn the webpage into a string for navigation purposes

for link in get_soup(URL).find_all('a'): #find all <a> tags. <a> tags are where hyperlinks (clickable links) are located in HTML format. 
    file_link = link.get('href')
    if FILETYPE in file_link: #If the file type is found in the link, then continue. In this example "If .csv is found in the <a> tag execute next line"
        print(file_link)
        with open(link.text, 'wb') as file:
            wget.download(file_link) #download and store file on local drive. 
