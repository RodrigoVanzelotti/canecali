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

time.sleep(5)
email = driver.find_element(By.ID, 'mail_address').get_attribute('value')

driver.execute_script('''window.open("https://thenewscc.com.br/indicacao/?grsf=c0r3yl","_blank");''')
time.sleep(5)
driver.find_element(By.ID, 'form-field-email').send_keys(email)
driver.find_element(By.XPATH, '//*[contains(text(), "confirmar")]').click()

driver.switch_to.window(driver.window_handles[0])


driver.close()
driver.quit()

# driver.get('https://thenewscc.com.br/indicacao/?grsf=c0r3yl')



time.sleep(15)