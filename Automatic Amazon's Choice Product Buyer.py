import time
import pyautogui as pag
from selenium import webdriver

val = input('Enter your search phrase:')
Email_Id = input('Enter your Amazon id:')
Password = input('Enter your Amazon password:')
driver = webdriver.Chrome("E:\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.amazon.in/')
time.sleep(1)
search_bar = driver.find_element_by_class_name("nav-fill")
search_bar.click()
pag.write(val)
pag.press('enter')
time.sleep(1)
Amazon_Choice = driver.find_element_by_id('B07HGGYWL6-amazons-choice-label').click()
time.sleep(1)
driver.find_element_by_id('buy-now-button').click()
time.sleep(1.5)
driver.find_element_by_id('ap_email').click()
pag.write(Email_Id)
pag.press('enter')
time.sleep(1)
driver.find_element_by_id('ap_password').click()
pag.write(Password)
pag.press('enter')
