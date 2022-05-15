from selenium import webdriver
import chromedriver_autoinstaller
import time   

#Important variables
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(3)

#Amounts
cursors = 0
grannies = 0
farms = 0
mines = 0
factories = 0
banks = 0
temples = 0
towers = 0
ships = 0
labs = 0

used_upgrades = 0

#Get prices
def get_cookies():
    cookie_count = list(driver.find_element_by_id("cookies").text)
    nums = [str(x) for x in range(0, 10)]
    amount = []
    for i in cookie_count:
        if i != ',' and i != '.':
            if i != 'c':
                amount.append(i)

            else:
                amount = ''.join(amount)

                if ''.join(list(amount)[5:]) == 'million':
                    amount = ''.join(list(amount)[:5])
                    amount = int(amount) * 1000

                return int(amount) 

def get_cursor_price():
    cursor_price = list(driver.find_element_by_id("productPrice0").text)
    cursor_price = int(''.join([x for x in cursor_price if x != ',']))
    return cursor_price

def get_granny_price():
        granny_price = list(driver.find_element_by_id("productPrice1").text)
        granny_price = int(''.join([x for x in granny_price if x != ',']))
        return granny_price

def get_farm_price():
    farm_price = list(driver.find_element_by_id("productPrice2").text)
    farm_price = int(''.join([x for x in farm_price if x != ',']))
    return farm_price

def get_mine_price():
    mine_price = list(driver.find_element_by_id("productPrice3").text)
    mine_price = int(''.join([x for x in mine_price if x != ',']))
    return mine_price

def get_factory_price():
    factory_price = list(driver.find_element_by_id("productPrice4").text)
    factory_price = int(''.join([x for x in factory_price if x != ',']))
    return factory_price

def get_bank_price():
    bank_price = list(driver.find_element_by_id("productPrice5").text)
    bank_price = int(''.join([x for x in bank_price if x != ',']))
    return bank_price

def get_temple_price():
    temple_price = list(driver.find_element_by_id("productPrice6").text)
    temple_price = int(''.join([x for x in temple_price if x != ',']))
    return temple_price

def get_tower_price():
    tower_price = list(driver.find_element_by_id("productPrice7").text)
    tower_price = int(''.join([x for x in tower_price if x != ',']))
    return tower_price

def get_ship_price():
    ship_price = list(driver.find_element_by_id("productPrice8").text)
    ship_price = int(''.join([x for x in ship_price if x != ',']))
    return ship_price

def get_lab_price():
    lab_price = list(driver.find_element_by_id("productPrice9").text)
    lab_price = int(''.join([x for x in lab_price if x != ',']))
    return lab_price

#Purchase upgrades
def cursor0():
    global used_upgrades
    cursor = driver.find_element_by_id("upgrade0")
    if cursors >= 1 and used_upgrades == 0:
        cursor.click()
        used_upgrades+=1

#Purchases makers
def buy_cursor():
    global cursors
    cursor = driver.find_element_by_id("product0")
    cursor.click()
    cursors+=1

def buy_granny():
    global grannies
    granny = driver.find_element_by_id("product1")
    granny.click()
    grannies+=1

def buy_farm():
    global farms
    farm = driver.find_element_by_id("product2")
    farm.click()
    farms+=1

def buy_mine():
    global mines
    mine = driver.find_element_by_id("product3")
    mine.click()
    mines+=1

def buy_factory():
    global factories
    factory = driver.find_element_by_id("product4")
    factory.click()
    factories+=1

def buy_bank():
    global banks
    bank = driver.find_element_by_id("product5")
    bank.click()
    banks+=1

def buy_temple():
    global temples
    temple = driver.find_element_by_id("product6")
    temple.click()
    temples+=1

def buy_tower():
    global towers
    tower = driver.find_element_by_id("product7")
    tower.click()
    towers+=1

def buy_ship():
    global ships
    ship = driver.find_element_by_id("product8")
    ship.click()
    ships+=1

def buy_lab():
    global labs
    lab = driver.find_element_by_id("product9")
    lab.click()
    labs+=1

def is_affordable():
    if get_cookies() > get_cursor_price():
        buy_cursor()

    if get_cookies() > get_granny_price():
        buy_granny()

    try:
        if get_cookies() > get_farm_price():
            buy_farm()

        if get_cookies() > get_mine_price():
            buy_mine()

        if get_cookies() > get_factory_price():
            buy_factory()

        if get_cookies() > get_bank_price():
            buy_bank()
        
        if get_cookies() > get_temple_price():
            buy_temple()

        if get_cookies() > get_tower_price():
            buy_tower()

        if get_cookies() > get_ship_price():
            buy_ship()

        if get_cookies() > get_lab_price():
            buy_lab()

    except:
        pass

cookie = driver.find_element_by_id("bigCookie")
while True:
    cookie.click()
    is_affordable()