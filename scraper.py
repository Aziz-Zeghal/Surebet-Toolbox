from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from time import sleep
 
#--| Setup
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

#--| User input
b1 = input("What is your first bookmaker ?\n").upper()
while not isinstance(b1, str) :
    b1 = input("What is your first bookmaker ?\n")

b2 = input("What is your second bookmaker ?\n").upper()
while not isinstance(b2, str) :
    b2 = input("What is your second bookmaker ?\n")
    
print("------------------\n")

#--| Parse or automation
url = "https://www.betmonitor.com/surebets/"
driver.get(url)
element = driver.find_elements(by = By.CLASS_NAME, value = "surebet-cont")

"""Display example :

    Monday
    27 Mar
    18:00
    Basketball · Europe · Liga ABA
    CIBONA — FMP BEOGRAD
    O/U (Away) 85.5
     O
    2.22
    Highest: 1XBET
    2.67
    U
    1.65
    Highest: PINNACLE
    1.93
    12.0 %
    
"""

#We filter only the opportunities with the input bookmakers
opp = []
profit = []
for value in element :
    sure = value.text
    if sure.find(b1) != -1 and sure.find(b2) != -1 :
        print(sure)
        #We know that the profit is in the format XX.X %, so we grab the last 6 characters
        opp.append(sure)
        profit.append(float(sure[-6::].replace("%","")))
        print("------------------\n")
        
#--| Functions
driver.close()
driver.quit()