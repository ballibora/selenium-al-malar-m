import pandas as pd
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import *
import time

try:
    driver = webdriver.Firefox()

    sehirler_df = pd.read_excel("Tablolar.xls", sheet_name="t1")
    sehir_liste = sehirler_df["sehirler"].tolist()
    nufus = sehirler_df["nüfus"].tolist()

    yeni_df =pd.DataFrame( columns = ["şehir","kira sayisi","nüfus"])

    for il in sehir_liste :

        link = "https://www.sahibinden.com/kiralik-daire/"+ il.lower().replace("ı","i").replace("ü","u").replace("ğ","g").replace("ş","s").replace("ö","o").replace("ç","c")
        driver.get(link)
        kiralik=driver.find_element_by_xpath("/html/body/div[4]/div[4]/form/div/div[3]/div[1]/div[2]/div[1]/div[1]/span").text
        kiralik = kiralik[:-5].replace(".","")
        kiralik = int(kiralik)
        index = sehir_liste.index(il)
        il_nufus =int(nufus[index])
        

        eklenecek_df = pd.DataFrame([[il,kiralik,il_nufus]], columns= ["şehir","kira sayisi","nüfus"])
        print(eklenecek_df)
        yeni_df=yeni_df.append(eklenecek_df, ignore_index=True)
        print(yeni_df)
        time.sleep(randint(1,4))
        



except:
    print("hata")
finally:
    print(yeni_df.corr(method="kendall"))
    print(yeni_df.corr(method="pearson"))
    yeni_df.to_excel("sehir_kira_nüfus.xlsx")

    print("Finished")
