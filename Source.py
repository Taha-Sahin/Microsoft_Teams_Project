from selenium import webdriver
import sys
import selenium
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

import ctypes
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import json

Options().add_argument("--disable-infobars")

def error_message(message, title ):
    
    ctypes.windll.user32.MessageBoxW(0, message, title, 1)


    

try: 
    
    with open('config.json') as f:
        config = json.load(f)
except: 
    error_message("Couldn't loaded the config file. Please be sure that there is a config.json file in your file directory.", "JSON file Error")
    sys.exit(1)
    
try :
    service = Service("C:\Program Files (x86)\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
except: 
    error_message("Couldnt find the msedgedriver.exe in your C:\Program Files (x86) directory. Please be sure that it is a correct version or there is a exe file in that directory ", "msedgedriver Error")
    sys.exit(1)

URL_Teams = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=id_token&scope=openid%20profile&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=eyJpZCI6ImIzYzY5MjliLWJmYjYtNGE5NS05OGIyLTZlYmEyNWQ3ODFjOCIsInRzIjoxNjM3MjY5NjYwLCJtZXRob2QiOiJyZWRpcmVjdEludGVyYWN0aW9uIn0%3D&nonce=1c54841d-35f8-4eaa-bec2-4a83d69e51dd&client_info=1&x-client-SKU=MSAL.JS&x-client-Ver=1.3.4&client-request-id=e78a01ab-f8dc-4771-b328-0322d219bf73&response_mode=fragment"

def login_to_Teams():
    driver.get(URL_Teams)
    driver.implicitly_wait(15)
    
    try:
        driver.find_element(By.XPATH , "//input[@id='i0116']").send_keys(config["username"])
        Next = driver.find_element(By.XPATH, "//input[@id='idSIButton9']")
        if Next != None:
            Next.click()
    except:
        error_message("Please be sure that is it the correct username in config.json file.", "Username Error")
        
    try:    
        driver.find_element(By.XPATH, "//input[@id='i0118']").send_keys(config["password"])
        sleep(2)
        Sign_in = driver.find_element(By.ID, "idSIButton9")
        if Sign_in != None:
            Sign_in.click()
    except:
        error_message("Please be sure that is it the correct password in config.json file.", "Password Error")
        
    Yes = driver.find_element(By.XPATH, "//input[@id='idSIButton9']")
    if Yes != None:
        Yes.click()
        
    
        

        
    
        
    
    
    
    
    
    
login_to_Teams()
sleep(500)

