# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import re
'''
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

name = ""
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
names = []

n = int(input('Enter position: '))
if n < 1 or n > len(tags):
    print("Error: Invalid position.")
else:
    for i in range(n):
        # Look at the parts of a tag
        tag = tags[i]
        # print('TAG:', tag)
        # print('Retrieving:', tag.get('href', None))
        # print('Contents:', tag.contents[0])
        # print('Attrs:', tag.attrs)
        url = tag.get('href', None)
        # name = re.findall("known_by(.+).html", tag.contents)
        name = re.findall(r'by_(.+?).html', url)
        names.append(name[0])

print("Names are:", names[:n])
'''

url = input("Enter URL: ")
# url = "http://py4e-data.dr-chuck.net/known_by_Anmolpreet.html"
count = int(input("Enter count: "))
# count = 8
position = int(input("Enter position: "))
# position = 18
names = []
for i in range(count):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        url = tags[position - 1]['href']
        # Update the count value after each iteration
        count -= 1
    names.append(re.findall(r"known_by_(.*?)\.html", url))


# print("Last name in the list:", str(names[-1]))
