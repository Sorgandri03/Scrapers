import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

def FindLast(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    delay=20
    try:
        WebDriverWait(driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id=\"m74007478429\"]/figure/div[2]")))
    except TimeoutException:
        print ("Loading took too much time (first page)!")

    name = driver.find_element(By.XPATH,'//*[@id="m74007478429"]/figure/div[2]').get_attribute("aria-label")
    price = driver.find_element(By.XPATH,'//*[@id="m74007478429"]/figure/div[3]/div/span/span[2]').text
    link = driver.find_element(By.XPATH,'//*[@id="item-grid"]/ul/li[1]/div/a').get_attribute("href")
    
    driver.close()

    return name,price,link