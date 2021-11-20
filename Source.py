
from selenium import webdriver
import sys
import selenium

from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import ctypes
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

from time import sleep
import json


def xpath_find(XPATH):
    driver.find_element(By.XPATH, XPATH)
    
def xpath_find_click(XPATH):
    driver.find_element(By.XPATH, XPATH).click()
    
def xpath_find_send_keys(XPATH, Key):
    
    driver.find_element(By.XPATH, XPATH).send_keys(Key)

Options().add_argument("--disable-infobars")

def error_message(message, title ):
    
    ctypes.windll.user32.MessageBoxW(0, message, title, 1)


    

try: 
    
    with open('config.json') as f:
        config = json.load(f)
except: 
    error_message("Couldn't loaded the config file. Please be sure that there is a config.json file in your file directory.", "JSON file Error")
    sys.exit(1)


service = Service("C:\Program Files (x86)\msedgedriver.exe")
driver = webdriver.Edge(service = service)

action = ActionChains(driver)
URL_Teams = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=id_token&scope=openid%20profile&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=eyJpZCI6ImIzYzY5MjliLWJmYjYtNGE5NS05OGIyLTZlYmEyNWQ3ODFjOCIsInRzIjoxNjM3MjY5NjYwLCJtZXRob2QiOiJyZWRpcmVjdEludGVyYWN0aW9uIn0%3D&nonce=1c54841d-35f8-4eaa-bec2-4a83d69e51dd&client_info=1&x-client-SKU=MSAL.JS&x-client-Ver=1.3.4&client-request-id=e78a01ab-f8dc-4771-b328-0322d219bf73&response_mode=fragment"

def login_to_Teams():
    
    driver.get(URL_Teams)
    driver.implicitly_wait(20)
    
    try:
        driver.find_element(By.XPATH , "//input[@id='i0116']").send_keys("will be username")
        Next = driver.find_element(By.XPATH, "//input[@id='idSIButton9']")
        if Next != None:
            Next.click()
    except:
        error_message("Please be sure that is it the correct username in config.json file.", "Username Error")
        
    try:    
        driver.find_element(By.XPATH, "//input[@id='i0118']").send_keys("will be password")
        sleep(2)
        Sign_in = driver.find_element(By.ID, "idSIButton9")
        if Sign_in != None:
            Sign_in.click()
    except:
        error_message("Please be sure that is it the correct password in config.json file.", "Password Error")
        
    Yes = driver.find_element(By.XPATH, "//input[@id='idSIButton9']")
    if Yes != None:
        Yes.click()
    
def open_settings_menu():
            xpath_find_click("//button[@id='settings-menu-button']//ng-include//*[name()='svg']")
            xpath_find_click("//button[@class='ts-sym left-align-icon']")

def changing_list_view():
    driver.implicitly_wait(20)
    try:
        open_settings_menu()
        xpath_find_click("//li[@aria-label='List layout button']")
        xpath_find_click("//button[@title='Close']")
    except:
        driver.refresh()
        
    
def search_for_expanded():
    driver.implicitly_wait(20)
    driver.find_element(By.ID, "app-bar-2a84919f-59d8-4441-a975-2a8c2643b741").click()
    xpath_find_click("//button [@class ='ts-sym app-icons-fill-hover left-rail-header-filter-button left-rail-header-button']")
    xpath_find_click("//input[@id='left-rail-header-filter-input']")
    Channel = driver.find_elements(By.XPATH, '//span [@class = "truncate header-text"]')
    is_it_expanded = driver.find_elements(By.XPATH, '//li [@class="match-parent team left-rail-item-kb-l2"]')
    
    for i in range(len(Channel)):#for closing all sub channel 
        action.move_to_element(Channel[i])
        action.perform()
        check_expanded = is_it_expanded[i].get_attribute('aria-expanded')
        if( check_expanded == "true"):
            action.click()
            sleep(0.5)
def search_for_meeting():
    driver.implicitly_wait(20)
    driver.find_element(By.ID, "app-bar-2a84919f-59d8-4441-a975-2a8c2643b741").click()
    xpath_find_click("//button [@class ='ts-sym app-icons-fill-hover left-rail-header-filter-button left-rail-header-button']")
    xpath_find_click("//input[@id='left-rail-header-filter-input']")
    Channel = driver.find_elements(By.XPATH, '//span [@class = "truncate header-text"]')
    for a in range (len(Channel)):#for search recent meeting
        action.move_to_element(Channel[a])
        action.click()
        action.perform()
        sleep(5)
        Channels = driver.find_elements(By.XPATH, '//span [@class = "truncate"]')
        for j in range(len(Channels)):
            action.move_to_element(Channels[j])
            action.click()
            action.perform()
            sleep(0.5)
            
                

            
               
        action.move_to_element(Channel[a])
        action.click()
        action.perform()
        sleep(0.5) 
        
    
  
      
    
login_to_Teams()
changing_list_view()
search_for_expanded()
search_for_meeting()

sleep(500)