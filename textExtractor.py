# import BeautifulSoup 
# from urllib.request import urlopen
# url = "http://kite.com"
# html = urlopen(url).read()
# soup = BeautifulSoup(html)

# for script in soup(["script", "style"]):
#     script.decompose()



# strips = list(soup.stripped_strings)
# print(strips[:5])

import re
from urllib.request import urlopen

url = "https://codeforces.com/"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)