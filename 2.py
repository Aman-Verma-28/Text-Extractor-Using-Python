import re
import urllib.request
import urllib.parse
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup



# opener = urllib2.build_opener()
# opener.addheaders = [{"User-agent", 'Mozilla/5.0'}]

# url = (https://codeforces.com/)
# openUrl = opener.open(url).read()

# soup = BeautifulSoup(openUrl)

# title = soup.title.text

# body = soup.findall('p')
# outfile = open("some.txt",'w')

# for i in body:
#     i=i.text
#     i=re.sub("\[\d+\]", " ",str(i))
#     i=re.sub("\[.*?\]", " ",str(i))
#     outfile.write(str(i)+"\n")

url = 'view-source:https://www.youtube.com/watch?v=0lgPB53c9RY'
page = urlopen(url)

html = BeautifulSoup(page)

print(html.prettify)
print(html.title.string)