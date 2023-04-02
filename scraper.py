from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from time import sleep
 
#--| Setup
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

#--| User input
b1 = input("What is your first bookmaker ?\n").split(" ")[0].upper()
while not isinstance(b1, str) :
    b1 = input("What is your first bookmaker ?\n")

b2 = input("What is your second bookmaker ?\n").split(" ")[0].upper()
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
for value in element :
    sure = value.text
    
    if sure.find(b1) != -1 and sure.find(b2) != -1 and sure.find("3-Way") == -1:
        info = sure.split("\n")
        time = info[1] + " " + info[2]
        match = info[3] + " " + info[4]
        typebet = info[5]
        
        #Sometimes, we have additional info, so we need to find the bookmaker indexes
        bm1 = info.index("Highest: " + b1)
        bm2 = info.index("Highest: " + b2)
        
        bm1 = "On " + info[bm1] + " for " + info[bm1 + 1]
        bm2 = "On " + info[bm2] + " for " + info[bm2 + 1]
        profit = sure[-6::]
        opp.append((time, match, typebet, bm1, bm2, profit))

driver.close()
driver.quit()
if opp == [] :
    print("Nothing right now !\n")

#--| Functions
def print_opp() :
    for arb in opp :
        print("⏲ " + arb[0]) #time
        print("🏟 " + arb[1] + "\n") #match
        print(arb[2] + "\n") #typebet
        print(arb[3]) #bookmaker1
        print(arb[4] + "\n") #bookmaker2
        print("💲 " + arb[5] + "\n") #profit
        print("------------------\n")

print_opp()