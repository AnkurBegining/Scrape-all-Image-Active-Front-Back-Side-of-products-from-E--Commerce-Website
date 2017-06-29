from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()

# Url from which i will scrap my data
myUrl = "https://www.titan.co.in/shop-online/watches/titan"
browser.get(myUrl)
