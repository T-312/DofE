import openpyxl
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

os.chdir("/Users/tim10/Documents")

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.suggestmemovie.com/")

wb = openpyxl.load_workbook("Movies.xlsx")
ws = wb["Sheet1"]
data = []
all_data = []

a = 0
b = 0

while a != 100:
    a+=1
    b+=1
    time.sleep(3)
    name = driver.find_element_by_tag_name("h1")    
    rating = driver.find_element_by_class_name("display-1.my-1")
    genres = driver.find_element_by_class_name("h3")

    name = name.text.split()
    date = name[-1]    
    name.remove(name[-1])
    name = ' '.join(name)

    if name in all_data:
        data.clear()

    if name not in all_data:
        data.append(name)
        data.append(int(date))
        data.append(float(rating.text))
        data.append(genres.text)
        
        all_data.append(name)

        print("---------------------")
        print(name)
        print(date)
        print(genres.text)
        print("---------------------")

        ws.append(data)
        data.clear()
        driver.refresh()
        print("Completion: ", b, "%", sep="")

    if a == 100:
        driver.quit()
        wb.save("Movies.xlsx")
        wb.close()