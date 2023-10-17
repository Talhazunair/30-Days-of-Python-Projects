from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import os
os.environ['Path'] += r"G:\Talha Projects\Selenium\geckodriver.exe"
driver=webdriver.Firefox()
driver.get("https://www.facebook.com/")
time.sleep(10)
email_input=driver.find_element(By.ID,"email")
time.sleep(3)
password_input=driver.find_element(By.ID,"pass")
time.sleep(3)
login_btn_click = driver.find_element(By.NAME,"login")
email_input.send_keys("your facebook email")
time.sleep(3)
password_input.send_keys("your password")
time.sleep(3)
login_btn_click.click()
