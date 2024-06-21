# Surebet-Toolbox
This repository contains tools related to surebetting, valuebetting and other strategies using data analysis.

Will clean up READMEs and files later.

## Betmonitor-Surebet
Betmonitor scraper retrieves all arbitrage opportunites for input bookmakers<br>
Current version takes 2 input, bookmaker1 and bookmaker2<br>
No verification is done so put the right names<br>

Scraper.py will return all surebets with both bookmakers<br>
Bet type can be 1X2, under/over, etc.

### Todo
  - Optimize surebet container retrieval using XPATH<br>
  - For every container, click the calculator button to check if alternatives have bookmaker1 and bookmaker2<br>
  - Function to run 24/7, and check every x seconds the website<br>
  - Telegram notification for new opportunities on selected bookmakers (maybe idk) <br>

### Goal
The purpose of this project is to gain proficiency in using Selenium to scrape website data efficiently and effectively<br>
I plan to apply my knowledge of Selenium in more complex web crawling projects in the future
