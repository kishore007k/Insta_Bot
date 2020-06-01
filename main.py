from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()

website = driver.get('https://www.instagram.com/')
driver.implicitly_wait(5)

USERNAME = 'Your user name'
PASSWORD = 'your password'


user_name = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(USERNAME)
password = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(PASSWORD)

login_button = driver.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
sleep(5)

# If in case any popup comes up use the below code
pop_up = driver.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/div/div/div/button').click()
driver.implicitly_wait(2)
not_now = driver.find_element_by_xpath(
    '/html/body/div[4]/div/div/div[3]/button[2]').click()
sleep(5)

driver.quit()
