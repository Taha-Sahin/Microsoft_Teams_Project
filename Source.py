from selenium import webdriver
import sys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import ctypes
from selenium.webdriver.common.by import By
from time import sleep
import json

delay = 0
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
  })
print("""MIT License

Copyright (c) 2021 Taha SAHIN 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.\n\n\n\n\n""")

def error_message(message, title ):
    ctypes.windll.user32.MessageBoxW(0, message, title, 1)
try: 
    with open('config.json') as f:
        config = json.load(f)
except: 
    error_message("Couldn't loaded the config file. Please be sure that there is a config.json file in your file directory.", "JSON file Error")
    sys.exit(1)

def reset_password():
    pass
    
def intro_and_login():
    print("Welcome to the Teams Automater. ")    
    if(config['username'] == "Username"):
        while True:
            username = input("Please enter your teams mail: ")
            print('Are you sure about this is the right mail ? Press Y for yes ,no N')
            checkmail = input()
            if(checkmail == 'y' or checkmail == 'Y'):
                config['username'] = username
                break    
        with open ('config.json', 'w') as f:
            json.dump(config, f, indent= 4)
    if (config['password'] == "Password"):
        while True:
            password = input ("Please enter your teams password: ")
            print("Are you sure about this is the right mail ? Press Y for yes, no N") 
            checkpass = input()
            if(checkpass == 'y' or checkpass == 'Y'):
                config['password'] = password 
                break
        with open('config.json', 'w') as f:
            json.dump(config, f, indent= 4)
    print(f"Account: {config['username']}")
    
    

def delayfunc():
    while True:
        try:
            delay = float(input("\nPlease enter the delay that you want to start the program.(In minutes 'Example: 10'. Write 0 for instant run.) = ?\n"))
            break
        except:
            print("\n This is not a valid input. Please try to write just number. NOT WRİTE(Exp. '1 minute, 1 min , 1mint')")
    if(delay != 0):        
        print(f"\nDone. The program will be start after {delay} minutes... \n")
        sleep(delay*60)
      
intro_and_login()
delayfunc()

def xpath_find(XPATH):
    driver.find_element(By.XPATH, XPATH)
    
def xpath_find_click(XPATH):
    driver.find_element(By.XPATH, XPATH).click()
    
def xpath_find_send_keys(XPATH, Key):
    driver.find_element(By.XPATH, XPATH).send_keys(Key)
srvice = Service(".\msedgedriver.exe")
driver = webdriver.Edge(service = srvice, options= opt) 

action = ActionChains(driver)
URL_Teams = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=id_token&scope=openid%20profile&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=eyJpZCI6ImIzYzY5MjliLWJmYjYtNGE5NS05OGIyLTZlYmEyNWQ3ODFjOCIsInRzIjoxNjM3MjY5NjYwLCJtZXRob2QiOiJyZWRpcmVjdEludGVyYWN0aW9uIn0%3D&nonce=1c54841d-35f8-4eaa-bec2-4a83d69e51dd&client_info=1&x-client-SKU=MSAL.JS&x-client-Ver=1.3.4&client-request-id=e78a01ab-f8dc-4771-b328-0322d219bf73&response_mode=fragment"

def login_to_Teams():
    
    driver.get(URL_Teams)
    driver.implicitly_wait(20)
    
    try:
        driver.find_element(By.XPATH , "//input[@id='i0116']").send_keys(config["username"])
        Next = driver.find_element(By.XPATH, "//input[@id='idSIButton9']")
        if Next != None:
            Next.click()
    except:
        error_message("Please be sure that is it the correct username", "Username Error")
        
    try:    
        driver.find_element(By.XPATH, "//input[@id='i0118']").send_keys(config["password"])
        sleep(2)
        Sign_in = driver.find_element(By.ID, "idSIButton9")
        if Sign_in != None:
            Sign_in.click()
    except:
        error_message("Please be sure that is it the correct password", "Password Error")
    try:
        driver.implicitly_wait(10)
        Yes = driver.find_element(By.XPATH, "//input[@id='idSIButton9']")
        if Yes != None:
            Yes.click()
    except:
        pass
    
    try: 
        driver.implicitly_wait(10)
        use_app = xpath_find("//a[@class='use-app-lnk']")
        action.move_to_element(use_app)
        action.click()
        action.perform()
    except:
        pass
    
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
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "app-bar-2a84919f-59d8-4441-a975-2a8c2643b741").click()
    xpath_find_click("//button [@class ='ts-sym app-icons-fill-hover left-rail-header-filter-button left-rail-header-button']")
    xpath_find_click("//input[@id='left-rail-header-filter-input']")
    Channel = driver.find_elements(By.XPATH, '//span [@class = "truncate header-text"]')
    is_it_found = True
    while(is_it_found):
        for a in range (len(Channel)):#for search recent meeting
            action.move_to_element(Channel[a])
            action.click()
            action.perform()
            Channels = driver.find_elements(By.XPATH, '//span [@class = "truncate"]')
            for j in range(len(Channels)):
                action.move_to_element(Channels[j])
                action.click()
                action.perform()
                try:
                    check = driver.find_element(By.XPATH, "//button[@title='Join call with video']")
                    if(check != None):
                        is_it_found = False
                        break 
                except:
                    continue
            if (is_it_found == False):
                channel_name = Channel[a].get_attribute('title')
                print(f"You are joining the {channel_name}")
                break
            
            action.move_to_element(Channel[a])
            action.click()
            action.perform()

def join_meeting():
    driver.implicitly_wait(5)
    xpath_find_click("//button[@title='Join call with video']")
    xpath_find_click('//button [@class="ts-btn ts-btn-fluent ts-btn-fluent-secondary-alternate"]')
    xpath_find_click('//button [@class="join-btn ts-btn inset-border ts-btn-primary"]')
    xpath_find_click("//button[@id='roster-button']//ng-include[@class='iconWrapper']//*[name()='svg']")
        
def quit_meeting():
    max_people_amount = 0
    check_val = True
    while(check_val):
        driver.implicitly_wait(5)
        current_people = driver.find_elements(By.XPATH, '//li [@class="item vs-repeat-repeated-element" ]')
        print(f"Current people = {len(current_people)}")
        if(len(current_people) > max_people_amount):
            max_people_amount = len(current_people)
        threshold_value= (3*max_people_amount)/10
        print(f"Max people that joined the meeting = {max_people_amount}")
        print(f"Threshold value = {threshold_value}")
        if(len(current_people) <= threshold_value):
            xpath_find_click("//button[@id='hangup-button']//ng-include[@class='iconWrapper']//*[name()='svg']//*[name()='path' and contains(@class,'icons-defa')]")
            check_val = False
            break
        sleep(5)
    
    
        

login_to_Teams()
changing_list_view()
search_for_expanded()
search_for_meeting()
join_meeting()
quit_meeting()









