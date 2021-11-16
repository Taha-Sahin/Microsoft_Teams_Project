from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('C:\Program Files (x86)\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url='https://www.google.com'
driver.get(url)

search = driver.find_element_by_name("q")
search.send_keys("test")
