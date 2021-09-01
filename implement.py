import PyPDF2
import requests
from io import BytesIO
import io

pdf_link = 'https://agricoop.nic.in/sites/default/files/Hindi%20version%20of%20The%20Farmers%20%28E%26P%29%20Agreement%20on%20Price%20Assurance%20%281%29_1.pdf'

response = requests.get(pdf_link)

pdf_obj = PyPDF2.PdfFileReader(BytesIO(response.content))

# print the number of pages
# print(pdf_obj.numPages)

for page_num in range(pdf_obj.numPages):
    with io.open("texts2.txt", "a+", encoding="utf-8") as f:
        pdf_page = pdf_obj.getPage(page_num)
        f.write(pdf_page.extractText())
        # print('Page num: ' + str(page_num))
        # print(pdf_page.extractText())
    