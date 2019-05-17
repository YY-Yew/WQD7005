import requests
import re
       
url2 ='https://www.malaysiastock.biz/Annual-Report.aspx?'
response = requests.get(url2)   
response.status_code
url=response.text

print(url)

m = re.findall(r'(?i)(https?://.+?.pdf.+?.pdf)',url)

for list in m:
    pdfurl = list
    response = requests.get(pdfurl)
    with open(list[list.index("name=")+5:], 'wb') as f:
        f.write(response.content)
