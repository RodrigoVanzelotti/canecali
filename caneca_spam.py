from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from datetime import date, datetime
import time
import re
import json
import os

chrome_options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://10minutemail.com/")

time.sleep(10)
try:
    email = driver.find_element(By.ID, 'mail_address').get_attribute('value')
except:    
    time.sleep(10)
    email = driver.find_element(By.ID, 'mail_address').get_attribute('value')

driver.execute_script('''window.open("https://thenewscc.com.br/indicacao/?grsf=c0r3yl","_blank");''')
driver.switch_to.window(driver.window_handles[1])
continuar = False
while not continuar:
    try:
        driver.find_element(By.NAME, 'form_fields[email]').send_keys(email)
        driver.find_element(By.XPATH, '//*[contains(text(), "confirmar")]').click()
        continuar = True
    except:
        time.sleep(5)

time.sleep(20)
continuar = False
while not continuar:
    try:
        driver.find_element(By.CLASS_NAME, 'small_sender').click()
        driver.find_element(By.XPATH, '//*[contains(text(), "confirmar")]').click()
        continuar = True
    except:
        time.sleep(10)


driver.switch_to.window(driver.window_handles[0])


driver.close()
driver.quit()




# driver.get('https://thenewscc.com.br/indicacao/?grsf=c0r3yl')



time.sleep(15)