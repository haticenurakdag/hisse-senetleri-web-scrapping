from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json


browser = webdriver.Chrome()

URL="https://finans.mynet.com/borsa/hisseler/"
browser.get(URL)
time.sleep(5)

page_source=browser.page_source
soup=BeautifulSoup(page_source, "html.parser")
data_list=[]

strongs = soup.find_all("strong")
for strong in strongs:
    a_elements=strong.find_all("a")
    for a_element in a_elements:
        links=a_element.get("href")
        span=a_element.find("span")
        dict={"link":links, "başlık":span.text}

        browser.get(links)
        page_source_2=browser.page_source
        link_soup=BeautifulSoup(page_source_2, "html.parser")
        li_elements=link_soup.find_all("li", attrs={"class":"flex align-items-center justify-content-between"})
        for li_element in li_elements:
            span=li_element.find_all("span")
            for i in range(0,len(span),2):
                # print(span[i].text)
                # print(span[i+1].text)
                key=span[i].text
                value=span[i+1].text
                dict[key]=[value]
    data_list.append(dict)




with open ("hisse_senedi.json","w",encoding="utf-8") as json_file:
    json.dump(data_list,json_file,indent=4,ensure_ascii=False)







# for strong in strongs:
    # a_elements=strong.find_elements(By.TAG_NAME, "a")
    # for a_element in a_elements:
    #     link= a_element.get_attribute("href")
    #     print(link)
    # title = strong.find_element(By.TAG_NAME, "span")
    # print(title.text)

browser.close()
