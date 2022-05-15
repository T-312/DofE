import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

PIN = 936528
USERNAME = '-'

driver.get('https://kahoot.it/')

try:
    element_present = EC.presence_of_element_located((By.ID, 'game-input'))
    WebDriverWait(driver, 15).until(element_present)

except TimeoutException:
    exit()

pin = driver.find_element(By.ID, 'game-input')
pin.send_keys(PIN)
pin.send_keys(Keys.RETURN)
# .send_keys(USERNAME)