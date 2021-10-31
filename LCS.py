import requests
from bs4 import BeautifulSoup
import sqlite3
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# Uses Selenium to scroll webpage so all HTML loads
options = webdriver.ChromeOptions()



driver = webdriver.Chrome(options=options)

driver.get("https://www.factor.gg/players")
driver.execute_script("window.scrollTo(0, 1200)")
page_source = driver.page_source

#Gets soup object for parsing
soup = BeautifulSoup(page_source, 'html.parser')
#Creates/connects DB
conn = sqlite3.connect('LCS_Summer.db')


cursor = conn.cursor()
#Creating Table
cursor.execute("""CREATE TABLE IF NOT EXISTS players (Name varchar(255), Average_Gold INTEGER, 
Average_Gold_at_15 INTEGER,Average_GD_At_15 INTEGER, 
 Average_Assists INTEGER, Average_Damage_Per_Teamfight INTEGER, Average_Deaths INTEGER, 
 Average_Damage_healed INTEGER, Average_DPM INTEGER, Average_Worthless_Deaths INTEGER, Average_kills INTEGER, 
 Average_CS INTEGER, Average_Minutes_Between_deaths INTEGER, Average_minutes_between_kills INTEGER, 
 Average_neutral_minion_kills INTEGER)""")


stats = []
names = []
c = 1
table_body = soup.find('table', attrs={'class': 'stats-table min-w-full'})
table_nm = soup.find('table', attrs={'stats-table w-40 md:w-64'})
#Inserts data into DB
while c < 26:
    for row in table_nm.find_all('tr')[c]:
        names.append(row.getText().strip())
    for row1 in table_body.find_all('tr')[c]:
        stats.append(row1.getText().strip())
    cursor.execute("""INSERT INTO players 
            (Name, Average_Gold, Average_Gold_at_15,
             Average_GD_At_15, Average_Assists,Average_Damage_Per_Teamfight,
             Average_Deaths,Average_Damage_healed, Average_DPM,Average_Worthless_Deaths, Average_Kills,
             Average_CS,Average_Minutes_Between_deaths, Average_minutes_between_kills, Average_neutral_minion_kills
               ) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                   (names[1], stats[2], stats[3], stats[4], stats[5], stats[6], stats[7],
                    stats[8], stats[9], stats[10], stats[11], stats[12], stats[13],
                    stats[14], stats[15]))
    conn.commit()
    c += 1
    stats.clear()
    names.clear()
time.sleep(10)
#Goes to second page
l = driver.find_element(By.LINK_TEXT, '2')
l.click()
page_source = driver.page_source


soup1 = BeautifulSoup(page_source, 'html.parser')
table_body = soup1.find('table', attrs={'class': 'stats-table min-w-full'})
table_nm = soup1.find('table', attrs={'stats-table w-40 md:w-64'})
c = 1
#inserts second page into DB
while c < 11:
    for row in table_nm.find_all('tr')[c]:
        names.append(row.getText().strip())
    for row1 in table_body.find_all('tr')[c]:
        stats.append(row1.getText().strip())
    cursor.execute("""INSERT INTO players 
            (Name, Average_Gold, Average_Gold_at_15,
             Average_GD_At_15, Average_Assists,Average_Damage_Per_Teamfight,
             Average_Deaths,Average_Damage_healed, Average_DPM,Average_Worthless_Deaths, Average_Kills,
             Average_CS,Average_Minutes_Between_deaths, Average_minutes_between_kills, Average_neutral_minion_kills
               ) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                   (names[1], stats[2], stats[3], stats[4], stats[5], stats[6], stats[7],
                    stats[8], stats[9], stats[10], stats[11], stats[12], stats[13],
                    stats[14], stats[15]))
    conn.commit()
    c += 1
    stats.clear()
    names.clear()

