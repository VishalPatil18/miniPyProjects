import requests
from bs4 import BeautifulSoup


# ####**** Get the Html from web ****####
url = input('Enter Url: ')
r = requests.get(url)
htmlcontent = r.content
print(htmlcontent)


# ####**** Parse the Html ****####
soup = BeautifulSoup(htmlcontent,  'html.parser')
print(soup)
print(soup.prettify)


# ####**** Html tree traversal ****####
title = soup.title
print('title: ', title, ' type: ', type(title))

# get all paras from the text
paras = soup.find_all('p')
print(paras)

# it gives the first occurance of any tag
print(soup.find('p'))
print(soup.find('p')['class'])

# find all elements with a specific class eg.lead
print(soup.find_all('p', class_='lead'))

# get text from the elements/tags
print(soup.find('p').get_text())

# get all links from the anchors
an = soup.find_all('a')
links = set()
for link in an:
    if link.get('href') != '#' or link.get('href') != '/':
        links.add("https://codewithharry.com"+link.get('href'))
for x in links:
    print(x)

# get content from any elements using their id
navbarSupportedContent = soup.find(id='navbarSupportedContent')
for item in navbarSupportedContent.strings:
    print(item)
for item in navbarSupportedContent.stripped_strings:
    print(item)

# print any tag with given id eg. navbarSupportedContent
print(navbarSupportedContent.parent)

# next sibling and prev sibling
print(navbarSupportedContent.next_sibling)
print(navbarSupportedContent.previous_sibling)
print(navbarSupportedContent.previous_sibling.previous_sibling)

# get css selectors, attributes and classes
elem0 = soup.select('#loginModal')       # '#' is used for Modal
print(elem0)
elem1 = soup.select('.loginModal')       # '.' is used for class
print(elem1)
elem2 = soup.select('.modal-footer')
print(elem2)
