import time

from bs4 import BeautifulSoup as soup
from selenium import webdriver

# Open browser and get data
browser = webdriver.Firefox()

# Url from which i will scrap my data
myUrl = "https://www.titan.co.in/shop-online/watches/titan"
browser.get(myUrl)



for i in range(0, 50):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

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
