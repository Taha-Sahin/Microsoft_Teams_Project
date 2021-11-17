from selenium import webdriver
import sys
from selenium.webdriver.chrome.service import Service
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import json


try: 
    
    with open('config.json') as f:
        config = json.load(f)
except: 
    print("Config file have not found")
    sys.exit(1)
    
service = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service)


URL_Teams = "https://teams.microsoft.com/_#/calendarv2"

def login_to_Teams():
    driver.get(URL_Teams)
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH , "//input[@id='i0116']").send_keys("tahasahin")
    Next = driver.find_element(By.XPATH, "//input[@id='idSIButton9']")
    if Next != None:
        Next.click()
    driver.find_element(By.XPATH, "//input[@id='i0118']").send_keys(config["password"])
    Sign_in = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]" )
    if Sign_in != None:
        Sign_in.click()
    Yes = driver.find_element(By.XPATH, "//input[@id='idSIButton9']")
    if Yes != None:
        Yes.click()
        
    
    
    
    
    
    
login_to_Teams()
sleep(100)

