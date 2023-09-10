from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
table = soup.find_all('table')[1]
title = table.find_all('th')
z = [i.text.strip() for i in title]

data_frame = pd.DataFrame(columns = z)


data = table.find_all('tr')
for row in data[1:]:
    row_data = row.find_all('td')
    individual_data = [p.text.strip() for p in row_data]

    length = len(data_frame)
    data_frame.loc[length] = individual_data

print(data_frame)
data_frame.to_csv(r'C:\Users\Muhammad Satrio\Documents\Aku\Data Analysis\Data Sets\company_usa1.csv', index = False)
