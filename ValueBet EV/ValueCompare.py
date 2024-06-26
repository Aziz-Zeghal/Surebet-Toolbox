from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from time import sleep
import json

# To save session (remove headless operation):
"""
cookies = driver.get_cookies()


# Store cookies in a file
with open('cookies.json', 'w') as file:
    json.dump(cookies, file)
"""

#--| Setup
options = Options()
driver = webdriver.Chrome(options=options)
# options.add_argument("--headless")

# Load cookies from a file
with open('cookies.json', 'r') as file:
    cookies = json.load(file)



url ="https://fr.surebet.com/valuebets?utf8=%E2%9C%93&filter%5Bselected%5D%5B%5D=&filter%5Bselected%5D%5B%5D=34011237&filter%5Bsave%5D=&filter%5Bcurrent_id%5D=34011237&selector%5Border%5D=overvalue_desc&selector%5Bmin_group_size%5D=10&selector%5Bsettled_in%5D=0&selector%5Bmin_odds%5D=&selector%5Bmax_odds%5D=&selector%5Bmin_probability%5D=&selector%5Bmax_probability%5D=&selector%5Bmin_overvalue%5D=&selector%5Bmax_overvalue%5D=&selector%5Bbookies_settings%5D=0%3A67%3A%3A%3B0%3A105%3A%3A%3B0%3A253%3A%3A%3B0%3A231%3A%3A%3B0%3A66%3A%3A%3B0%3A76%3A%3A%3B0%3A93%3A%3A%3B0%3A182%3A%3A%3B0%3A74%3A%3A%3B0%3A37%3A%3A%3B0%3A148%3A%3A%3B0%3A211%3A%3A%3B0%3A114%3A%3A%3B0%3A260%3A%3A%3B0%3A101%3A%3A%3B0%3A132%3A%3A%3B0%3A42%3A%3A%3B0%3A40%3A%3A%3B0%3A225%3A%3A%3B0%3A269%3A%3A%3B0%3A126%3A%3A%3B0%3A201%3A%3A%3B0%3A21%3A%3A%3B0%3A70%3A%3A%3B0%3A263%3A%3A%3B0%3A23%3A%3A%3B0%3A111%3A%3A%3B0%3A246%3A%3A%3B0%3A26%3A%3A%3B0%3A296%3A%3A%3B0%3A236%3A%3A%3B0%3A139%3A%3A%3B0%3A36%3A%3A%3B0%3A150%3A%3A%3B0%3A202%3A%3A%3B0%3A151%3A%3A%3B0%3A204%3A%3A%3B0%3A309%3A%3A%3B0%3A125%3A%3A%3B0%3A200%3A%3A%3B0%3A203%3A%3A%3B0%3A60%3A%3A%3B0%3A116%3A%3A%3B0%3A32%3A%3A%3B0%3A138%3A%3A%3B0%3A1%3A%3A%3B0%3A65%3A%3A%3B0%3A161%3A%3A%3B0%3A301%3A%3A%3B0%3A29%3A%3A%3B0%3A10%3A%3A%3B0%3A107%3A%3A%3B0%3A106%3A%3A%3B0%3A265%3A%3A%3B0%3A45%3A%3A%3B0%3A228%3A%3A%3B0%3A34%3A%3A%3B0%3A77%3A%3A%3B0%3A58%3A%3A%3B0%3A165%3A%3A%3B0%3A100%3A%3A%3B0%3A153%3A%3A%3B0%3A95%3A%3A%3B0%3A311%3A%3A%3B0%3A180%3A%3A%3B0%3A254%3A%3A%3B0%3A208%3A%3A%3B0%3A14%3A%3A%3B0%3A197%3A%3A%3B0%3A152%3A%3A%3B0%3A11%3A%3A%3B0%3A188%3A%3A%3B0%3A291%3A%3A%3B0%3A38%3A%3A%3B0%3A147%3A%3A%3B0%3A52%3A%3A%3B0%3A198%3A%3A%3B0%3A300%3A%3A%3B0%3A304%3A%3A%3B0%3A55%3A%3A%3B0%3A187%3A%3A%3B0%3A33%3A%3A%3B0%3A13%3A%3A%3B0%3A185%3A%3A%3B0%3A68%3A%3A%3B0%3A176%3A%3A%3B0%3A248%3A%3A%3B0%3A215%3A%3A%3B0%3A49%3A%3A%3B0%3A113%3A%3A%3B0%3A62%3A%3A%3B0%3A75%3A%3A%3B0%3A12%3A%3A%3B0%3A177%3A%3A%3B0%3A193%3A%3A%3B0%3A157%3A%3A%3B0%3A90%3A%3A%3B0%3A46%3A%3A%3B0%3A279%3A%3A%3B0%3A229%3A%3A%3B0%3A210%3A%3A%3B0%3A146%3A%3A%3B0%3A117%3A%3A%3B0%3A255%3A%3A%3B0%3A135%3A%3A%3B0%3A24%3A%3A%3B0%3A282%3A%3A%3B0%3A88%3A%3A%3B0%3A73%3A%3A%3B0%3A171%3A%3A%3B0%3A53%3A%3A%3B0%3A261%3A%3A%3B0%3A144%3A%3A%3B0%3A312%3A%3A%3B0%3A121%3A%3A%3B0%3A154%3A%3A%3B0%3A104%3A%3A%3B0%3A129%3A%3A%3B0%3A234%3A%3A%3B0%3A56%3A%3A%3B0%3A170%3A%3A%3B0%3A276%3A%3A%3B0%3A108%3A%3A%3B0%3A230%3A%3A%3B0%3A22%3A%3A%3B0%3A290%3A%3A%3B0%3A158%3A%3A%3B0%3A307%3A%3A%3B0%3A145%3A%3A%3B0%3A136%3A%3A%3B0%3A30%3A%3A%3B0%3A219%3A%3A%3B0%3A273%3A%3A%3B0%3A257%3A%3A%3B0%3A5%3A%3A%3B0%3A6%3A%3A%3B0%3A274%3A%3A%3B0%3A214%3A%3A%3B0%3A112%3A%3A%3B0%3A245%3A%3A%3B0%3A295%3A%3A%3B0%3A235%3A%3A%3B0%3A175%3A%3A%3B0%3A224%3A%3A%3B0%3A190%3A%3A%3B0%3A294%3A%3A%3B0%3A297%3A%3A%3B0%3A183%3A%3A%3B0%3A264%3A%3A%3B0%3A242%3A%3A%3B0%3A213%3A%3A%3B0%3A244%3A%3A%3B0%3A15%3A%3A%3B0%3A212%3A%3A%3B0%3A128%3A%3A%3B0%3A315%3A%3A%3B0%3A233%3A%3A%3B0%3A50%3A%3A%3B0%3A9%3A%3A%3B0%3A259%3A%3A%3B0%3A179%3A%3A%3B0%3A178%3A%3A%3B0%3A41%3A%3A%3B0%3A85%3A%3A%3B0%3A169%3A%3A%3B0%3A84%3A%3A%3B0%3A266%3A%3A%3B0%3A130%3A%3A%3B0%3A133%3A%3A%3B0%3A247%3A%3A%3B0%3A3%3A%3A%3B0%3A281%3A%3A%3B0%3A280%3A%3A%3B0%3A131%3A%3A%3B0%3A240%3A%3A%3B0%3A271%3A%3A%3B4%3A8%3A%3A%3B0%3A118%3A%3A%3B0%3A89%3A%3A%3B0%3A283%3A%3A%3B0%3A285%3A%3A%3B0%3A284%3A%3A%3B0%3A166%3A%3A%3B0%3A299%3A%3A%3B0%3A124%3A%3A%3B0%3A226%3A%3A%3B0%3A209%3A%3A%3B0%3A82%3A%3A%3B0%3A63%3A%3A%3B0%3A83%3A%3A%3B0%3A98%3A%3A%3B0%3A99%3A%3A%3B0%3A61%3A%3A%3B0%3A167%3A%3A%3B0%3A137%3A%3A%3B0%3A258%3A%3A%3B0%3A141%3A%3A%3B0%3A164%3A%3A%3B0%3A19%3A%3A%3B0%3A142%3A%3A%3B0%3A278%3A%3A%3B0%3A249%3A%3A%3B0%3A39%3A%3A%3B0%3A174%3A%3A%3B0%3A31%3A%3A%3B0%3A54%3A%3A%3B0%3A194%3A%3A%3B0%3A251%3A%3A%3B0%3A51%3A%3A%3B0%3A181%3A%3A%3B0%3A103%3A%3A%3B0%3A2%3A%3A%3B0%3A143%3A%3A%3B4%3A7%3A%3A%3B0%3A122%3A%3A%3B0%3A162%3A%3A%3B0%3A172%3A%3A%3B0%3A237%3A%3A%3B0%3A168%3A%3A%3B0%3A156%3A%3A%3B0%3A272%3A%3A%3B0%3A293%3A%3A%3B0%3A47%3A%3A%3B0%3A305%3A%3A%3B0%3A134%3A%3A%3B0%3A306%3A%3A%3B0%3A218%3A%3A%3B0%3A302%3A%3A%3B0%3A123%3A%3A%3B0%3A94%3A%3A%3B0%3A310%3A%3A%3B4%3A25%3A%3A%3B0%3A69%3A%3A%3B0%3A313%3A%3A%3B0%3A140%3A%3A%3B0%3A119%3A%3A%3B0%3A16%3A%3A%3B0%3A207%3A%3A%3B0%3A287%3A%3A%3B0%3A232%3A%3A%3B0%3A48%3A%3A%3B0%3A223%3A%3A%3B0%3A256%3A%3A%3B0%3A163%3A%3A%3B0%3A97%3A%3A%3B0%3A191%3A%3A%3B0%3A173%3A%3A%3B0%3A186%3A%3A%3B0%3A192%3A%3A%3B0%3A270%3A%3A%3B0%3A43%3A%3A%3B0%3A243%3A%3A%3B0%3A267%3A%3A%3B0%3A199%3A%3A%3B0%3A91%3A%3A%3B0%3A289%3A%3A%3B0%3A275%3A%3A%3B0%3A184%3A%3A%3B0%3A18%3A%3A%3B0%3A59%3A%3A%3B0%3A64%3A%3A%3B0%3A216%3A%3A%3B0%3A314%3A%3A%3B0%3A86%3A%3A%3B0%3A120%3A%3A%3B0%3A277%3A%3A%3B0%3A149%3A%3A%3B0%3A127%3A%3A%3B0%3A115%3A%3A%3B0%3A17%3A%3A%3B0%3A160%3A%3A%3B0%3A110%3A%3A%3B0%3A238%3A%3A%3B0%3A102%3A%3A%3B0%3A239%3A%3A%3B0%3A217%3A%3A%3B0%3A303%3A%3A%3B0%3A206%3A%3A%3B0%3A96%3A%3A%3B0%3A28%3A%3A%3B0%3A222%3A%3A%3B0%3A220%3A%3A%3B0%3A250%3A%3A%3B0%3A252%3A%3A%3B0%3A44%3A%3A%3B0%3A196%3A%3A%3B0%3A308%3A%3A%3B0%3A227%3A%3A%3B0%3A155%3A%3A%3B0%3A195%3A%3A%3B0%3A221%3A%3A%3B0%3A71%3A%3A%3B0%3A79%3A%3A%3B0%3A80%3A%3A%3B0%3A78%3A%3A%3B0%3A81%3A%3A%3B0%3A27%3A%3A&selector%5Bexclude_sports_ids_str%5D=56+57+0+43+32+3+55+60+28+8+44+9+26+34+10+11+12+39+47+46+48+49+59+53+54+58+30+13+29+45+19+36+33+31+40+64+42+41+20+62+61+50+51+63+21+37+23+35+38&selector%5Btournaments%5D=&selector%5Btournaments_action%5D=group&selector%5Btournaments_group%5D=all&narrow="
driver.get(url)

# Set stored cookies to maintain the session
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

# Global variables
EV, tocompare = {}, []
def scrap():
    # Access
    try:
        elements = driver.find_elements(by = By.CLASS_NAME, value = "valuebet_record")
    except:
        driver.close()
        driver.quit()
        
    for elm in elements:
        splited = elm.text.split()
        # (probability, surevaluation)
        print(splited)
        if splited[-4].replace(',', '.')[:4:] == "péri":
            prob, surevaluation = splited[-2].replace(',', '.')[:4:], splited[-1].replace(',', '.')[:5:]
        else:
            prob, surevaluation = splited[-4].replace(',', '.')[:4:], splited[-3].replace(',', '.')[:5:]
        try:
            tocompare.append((float(prob) / 100, float(surevaluation) / 100, splited[4:10:]))
        except:
            continue
        
    for p, s, match in tocompare:
        EV[p * (1 + s)] = (match, round(p, 3), round(s, 3))

# Init
try:
    nextPage = driver.find_elements(by = By.CLASS_NAME, value = "next_page disabled")
    while nextPage == []:
        scrap()
        sleep(1)
        driver.find_elements(by = By.CLASS_NAME, value = "next_page")[0].click()
except:
    scrap()

# Print
for hot in sorted(EV, reverse=True):
    print(EV[hot])

"""

driver.close()
driver.quit()

"""
driver.close()
driver.quit()