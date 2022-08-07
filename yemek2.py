import pandas as pd
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from random import *
import time
import math
from yemek import *

driver = webdriver.Firefox()
hedef = "https://www.yemeksepeti.com/mersin/tantuni#ors:true"
driver.get(hedef)
elems = driver.find_elements_by_class_name("restaurantName ")
links = [elem.get_attribute('href') for elem in elems]
for link in links:
    toplayici(link,driver)




