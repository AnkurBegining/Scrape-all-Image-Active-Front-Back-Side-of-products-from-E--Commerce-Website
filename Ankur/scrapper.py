import os
import time
from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup
from selenium import webdriver

# Open browser and get data
browser = webdriver.Firefox()

# Url from which i will scrap my data
myUrl = "https://www.titan.co.in/shop-online/watches/titan"
browser.get(myUrl)

for i in range(0, 60):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    try:
        browser.find_element_by_link_text("Show more products").click()
    except:
        pass




'''HTML PARSING'''

# Parse html
page_soup = soup(browser.page_source, "html5lib")

'''Grab all products'''

containers = page_soup.find_all("div", {"class": "product"})
print("Number of watches found:: ", len(containers))

for contains in containers:
    try:
        product_page_link_container = contains.find('a', {'class': 'product_page_link'})
        product_detail_url = product_page_link_container['href']
        newUrl = myUrl + product_detail_url

        print(newUrl)

        openurl = uReq(newUrl)
        pageHtml = openurl.read()
        openurl.close()
        pageSoup = soup(pageHtml, 'html.parser')

        # Model Number
        ContainersForModel = pageSoup.find('p', {'class': 'stock'}).getText()
        ModelNumber = ContainersForModel.strip()
        PrefectModelNumber = ModelNumber[1:ModelNumber.index(')')]

        # Containers For Image
        ContainersForImage = pageSoup.find_all('li', {'class': 'thumbnail_image'})

        i = 0
        Directory = "/home/ankur/PycharmProjects/Download all Image(Active,Front,Side,Back etc) of product from E-Commerce WebSite/Ankur/Image Container"
        os.chdir(Directory)
        for contains in ContainersForImage:
            Image = contains.img['src']
            imageName = PrefectModelNumber + "_" + str(i)
            ImageFile = open(imageName + '.jpeg', 'wb')

            ImageFile.write(uReq(Image).read())
            ImageFile.close()
            i = i + 1
        i = 0
    except:
        pass

print("Ankur Ranjan")
