# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import json


# browser=webdriver.Chrome()
# URL="https://finans.mynet.com/borsa/hisseler/"
# browser.get(URL)
# data_list=[]

# strongs=browser.find_elements(By.TAG_NAME, "strong")
# links_and_titles = [] 
# for strong in strongs:
#     a_elements=strong.find_elements(By.TAG_NAME, "a")
#     for a_element in a_elements:
#         link=a_element.get_attribute("href")
#         span=a_element.find_element(By.TAG_NAME, "span")
#         links_and_titles.append({"link":link,"başlık":span.text})
# for link_info in links_and_titles:
#     link = link_info["link"]
#     browser.get(link)
    
            
#     try:
#         li_elements = WebDriverWait(browser, 20).until(
#             EC.presence_of_element_located((By.TAG_NAME, "li"))
#         )
#         data={}
#         for li_element in li_elements:
#             span=li_element.find_elements(By.TAG_NAME, "span")
            
#         for i in range(0,len(span),2):
#             key=span[i]
#             value=span[i]
#             data[key]=value
#         links_info(data)  
#         data_list.append(link_info)

#     except:
#         print("li dee hata oluştu")
#         # li_elements=browser.find_elements(By.TAG_NAME, "li")
        


# with open("selenium.json","w",encoding="utf-8") as json_file:
#     json.dump(data_list,json_file,indent=4,ensure_ascii=False)



# browser.close()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

browser=webdriver.Chrome()
URL="https://finans.mynet.com/borsa/hisseler/"
browser.get(URL)
time.sleep(5)
data_list=[]

strongs=browser.find_elements(By.TAG_NAME, "strong")
for strong in strongs:
    wait = WebDriverWait(browser, 10) 
    a_elements = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
    for a_element in a_elements:
        link = a_element.get_attribute("href")
        wait = WebDriverWait(browser, 10) 
        span = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "span")))
        # span=a_element.find_element(By.TAG_NAME, "span").text
        dict = {"link":link, "başlık":span}
        
        if link.startswith("http://") or link.startswith("https://"):
            browser.get(link)
        else:
            print("Unsupported protocol:", link)
            continue 

        wait = WebDriverWait(browser, 10)
        li_elements = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "li")))

        # li_elements=browser.find_elements(By.TAG_NAME,"li")
        for li_element in li_elements:
            span_elements=li_element.find_elements(By.TAG_NAME,"span")
           
            for i in range(0, len(span_elements)-1, 2):
                key = span_elements[i].text
                value = span_elements[i+1].text
                dict[key] = value
    data_list.append(dict)
browser.quit()
with open("selenium.json","w",encoding="utf-8") as json_file:
    json.dump(data_list,json_file,indent=4,ensure_ascii=False)





