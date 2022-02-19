import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')

if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/known_by_Lasse.html"         
count = int(input ('Enter count: '))
pos = int(input('Enter position: '))

cont1 = 0

while True:
    cont1 = cont1 + 1
    if cont1 > count:
        break   
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
    except: 
        print ('Invalid Address')
        exit ()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    cont2 = 0
    for tag in tags:
        cont2 = cont2 + 1
        if cont2 > pos:
            break
        url = (tag.get('href', None))
    print ('Retrieving: ' + url)

