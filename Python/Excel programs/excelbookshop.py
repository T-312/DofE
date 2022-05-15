import openpyxl
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

os.chdir("/Users/Tim/Desktop/Text Files/")

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome()
driver.get("http://books.toscrape.com/")

book = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[1]/article/h3/a")
book2 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[2]/article/h3/a")
book3 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[3]/article/h3/a")
book4 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[4]/article/h3/a")
book5 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[5]/article/h3/a")
book6 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[6]/article/h3/a")
book7 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[7]/article/h3/a")
book8 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[8]/article/h3/a")
book9 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[9]/article/h3/a")
book10 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[10]/article/h3/a")
book11 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[11]/article/h3/a")
book12 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[12]/article/h3/a")
book13 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[13]/article/h3/a")
book13 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[14]/article/h3/a")
book14 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[15]/article/h3/a")
book15 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[16]/article/h3/a")
book16 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[17]/article/h3/a")

a = 0
while a != 49:
    time.sleep(2)
    a+=1

    book = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[1]/article/h3/a")
    book.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

    book2 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[2]/article/h3/a")
    book2.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

    book3 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[3]/article/h3/a")
    book3.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

    book4 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[4]/article/h3/a")
    book4.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

    book5 = driver.find_element_by_xpath("/html/body/div/div/div/div/section/div[2]/ol/li[5]/article/h3/a")
    book5.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

    book6.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

    book7.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

    book8.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

    book9.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

    book10.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

    book11.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

    book12.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

    book13.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

    book14.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

    book15.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

    book16.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)


    next1 = driver.find_element_by_link_text("next").click()