import pandas as pd
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from random import *
import time
import math


def toplayici(link,driver):

    driver.get(link)
    sayi = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[4]/a")
    sayi = sayi.text
    sayi = sayi[10:-1]
    sayi = int(sayi)
    sayfa = math.ceil(sayi/30)
    isim = driver.find_element_by_class_name("restaurantName ")
    isim = isim.text
    print(isim+" "+":")    

    for page in range(1,sayfa+1):  
        site = link + "?section=comments&page="+f"{page}"
        driver.get(site)
        i = True
        n = 2
        while i is True:
            try:
                yorum = driver.find_element_by_xpath(f"/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[4]/div[4]/div[{n}]/div[1]/div[2]/p")
                yorum = yorum.text
                print(yorum)
                note = open(f"{isim}.txt" , "a")                
                note.write(yorum + "\n")
                note.close()
                n = n + 1

            except NoSuchElementException:
                i = False



