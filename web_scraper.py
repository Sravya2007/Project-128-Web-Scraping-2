from bs4 import BeautifulSoup
import requests
import pandas as pd

WEBSITE_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

webpage = requests.get(WEBSITE_URL, verify = False)

#MJ = Mass of Jupiter, M☉ = Mass of Sun
headers = ["Star Name", "Distance (ly)", "Mass(MJ)", "Radius (RJ)"]

soup = BeautifulSoup(webpage.content, "html.parser")

tables = soup.find_all('table', attrs = {"class" : "wikitable sortable"})

table = tables[2]

table_rows = table.find_all('tr')

star_list = []
for rows in table_rows:
    table_data = rows.find_all('td')

    row = [data.text.strip() for data in table_data]

    star_list.append(row)

star_names = []
distance = []
mass = []
radius = []

for table_data in range(1, len(star_list)):
    data = star_list[table_data]

    star_names.append(data[0])
    distance.append(data[5])
    mass.append(data[7])
    radius.append(data[8])

star_data = zip(star_names, distance, mass, radius)

star_data_list = pd.DataFrame(star_data, columns = headers)

star_data_list.to_csv("field_brown_dwarfs.csv", index = False)

print("Data scraped!")