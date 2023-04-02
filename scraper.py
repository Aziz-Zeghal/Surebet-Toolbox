from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from time import sleep
 
#--| Setup
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

#--| Parse or automation

url = "https://www.betmonitor.com/surebets/"
driver.get(url)
element = driver.find_elements(by = By.CLASS_NAME, value = "surebet-cont")

for value in element :
    print(value.text + "\n")


driver.close()
driver.quit()