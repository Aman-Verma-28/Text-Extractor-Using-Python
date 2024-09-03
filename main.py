import requests
from bs4 import BeautifulSoup
import io

url ="https://hi.vikaspedia.in/agriculture/91594393793f-90692793e93093f924-90992694d92f94b917/93094793692e-90992694d92f94b917/93094793692e-90992694d92f94b917-92f93e-93894793094091593294d91a930"
# url = "https://hi.vikaspedia.in/agriculture/91594393793f-90692793e93093f924-90992694d92f94b917/93094793692e-90992694d92f94b917/93094793692e-92e947902-92a93e92f940-91c93e928947-93593e932940-92c94092e93e93093f92f93e901-90f935902-93094b91592593e92e"
# url ="https://hi.vikaspedia.in/agriculture/91594393793f-90692793e93093f924-90992694d92f94b917/93094793692e-90992694d92f94b917/%E0%A4%B6%E0%A4%B9%E0%A4%A4%E0%A5%82%E0%A4%A4%E0%A5%80-%E0%A4%B0%E0%A5%87%E0%A4%B6%E0%A4%AE-%E0%A4%95%E0%A5%87-%E0%A4%B2%E0%A4%BF%E0%A4%8F-%E0%A4%86%E0%A4%B5%E0%A4%B6%E0%A5%8D%E0%A4%AF%E0%A4%95-%E0%A4%AE%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%97%E0%A4%A6%E0%A4%B0%E0%A5%8D%E0%A4%B6%E0%A4%BF%E0%A4%95%E0%A4%BE-null-1"
# url ="https://hi.vikaspedia.in/agriculture/policies-and-schemes/91594393793f-93094b91c91793e930-935-92a94d93093693f91594d937923/rural-employment"
html = requests.get(url, timeout=60).text

soup = BeautifulSoup(html, 'lxml')
paras = soup.find_all('p')
for i in paras:
    with io.open("test.txt", "a+", encoding="utf-8") as f:
        f.write(i.text+"\n")
print("Finished writing")
