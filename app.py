"""
bu modül mynet sitesindeki hisse senetlerinin bilgilerini çekerek 
bunları json dosyasına yazar
"""
import json
import requests
from bs4 import BeautifulSoup


URL= "https://finans.mynet.com/borsa/hisseler/"
response = requests.get(URL, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")
tbody_elements=soup.find_all("tbody", attrs={"class": "tbody-type-default"})
data_list=[]
for tbody in tbody_elements:
    strong_elements=tbody.find_all("strong")
    for strong in strong_elements:
        a_elements=strong.find_all(attrs={"href":True})
        span_elements=strong.find_all("span")
        link_texts=[link.get("href")for link in a_elements]
        span_texts=[span.get_text()for span in span_elements]
        for i, (link_text,span_text) in enumerate(zip(link_texts,span_texts)):
            data={"link":link_text,"başlık":span_text}
            detay=requests.get(link_text, timeout=10)
            detay_soup=BeautifulSoup(detay.text, 'html.parser')
            li_elements=detay_soup.find_all("li",
            attrs={"class":"flex align-items-center justify-content-between"})
            for li in li_elements:
                span_elements=li.find_all("span")
                for i in range(0,len(span_elements),2):
                    key=span_elements[i].get_text()
                    value=span_elements[i+1].get_text()
                    data[key]=value
            data_list.append(data)

with open("hisse_özellikler.json", "w", encoding="utf-8") as json_file:
    json.dump(data_list, json_file, indent=4, ensure_ascii=False)
