from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
table = soup.find_all('table')[1]
title = table.find_all('th')
z = [i.text.strip() for i in title]

df = pd.DataFrame(columns = z)


data = table.find_all('tr')
for row in data[1:]:
    row_data = row.find_all('td')
    individual_data = [p.text.strip() for p in row_data]

    length = len(df)
    df.loc[length] = individual_data

#see max rows and columns in dataframe
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# group company to Industry
#change data to float
df['Revenue (USD millions)'] = df['Revenue (USD millions)'].str.replace(',', '', regex=True).astype(float)
df['Employees'] = df['Employees'].str.replace(',', '', regex=True).astype(float)

#groupping by industry, top 10 industry by revenue
grouped_df = df.groupby("Industry")
summ = grouped_df[['Revenue (USD millions)']].sum()
srt = summ.sort_values(by="Revenue (USD millions)", ascending= False).head(10)
print(srt)

#groupping by headquarters, top 10 employees in headquarters by city and state
grouped_df2 = df.groupby("Headquarters")
summ2 = grouped_df2[['Employees']].sum()
srt2 = summ2.sort_values(by="Employees", ascending= False).head(10)
print(srt2)

#graphs
plt.style.use('dark_background')
srt.plot(kind = 'bar',title = 'Top 10 Industry by Revenue', xlabel = 'Industry', ylabel = 'Revenue')
plt.tight_layout()
srt2.plot(kind = 'bar',title = 'Top 10 City,State by Total Employees', xlabel = 'City, State', ylabel = 'Total Employees')
plt.tight_layout()
plt.show()

