from selenium import webdriver 
from selenium.webdriver.common.by import By  
from bs4 import BeautifulSoup  
import time 
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  
# import request module


browser = webdriver.Chrome()

scrapped_data = []  

bright_star_table = soup.find("table", attrs={"class", "wikitable"} )

table_body = bright_star_table.find('tbody')

table_rows = table_body.find_all('tr')

for row in table_rows:
    table_cols = row.find_all('td')
    #print(table_cols)

    temp_list = []

    for col_data in table_cols:
        #print(col_data.text)



        data = col_data.text.strip()
        #print(data)

        temp_list.append(data)

    scrapped_data.append(temp_list)


stars_data = []

for i in range(0, len(scrapped_data)):

    Star_names = scrapped_data[i][1]    
    Distance = scrapped_data[i][3]
    Mass = scrapped_data[i][5]
    Radius = scrapped_data[i][6]
    Lum = scrapped_data[i][7]

    required_data = ['Star names', ' Distance', "Mass", "Radius", "Luminosity"]
    stars_data.append(required_data)


headers = ['Star names', ' Distance', "Mass", "Radius", "Luminosity"]


star_df_1 = pd.DataFrame(stars_data, columns = headers)

star_df_1.to_csv('scared_data.csv', index = True, index_label = "id")





