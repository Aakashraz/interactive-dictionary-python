import requests
import json

# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Division by zero"
#
#
# print(divide(3, 2))


# password = " "
# while password != "password":
#     password = input("Enter your password: ")
#     if password == 'password':
#         print("Welcome back, {}".format(password))
#     else:
#         print("Wrong password")


# file = open('example.txt', 'w')
# file.write('hello')
# file.close()

# using the "with" to handle the file
# import os
#
# with open("example.txt", "w+") as f:
#     for i in range(29):
#         data = f.write("starline" + str(i+56) + '\n')
#     f.seek(0)
#     content = f.read()
#     print('write data: {} and read data: {}'.format(data, content))
#
# # delete the file
# if os.path.exists("example.txt"):
#     os.remove("example.txt")
#     print("removed example.txt")


# ---------------------------using date and time
# import datetime
# import time
#
# first = []
# for i in range(5):
#     # now().strftime will format the time accordingly
#     first.append(datetime.datetime.now().strftime("%Y %b %d %I:%M %p"))
#     time.sleep(1)
# for i in first:
#     print(i)  # to print in new lines

# --------------------------------json api call

# define the base URL and endpoints
base_url = "https://www.nrb.org.np/api/forex/v1/rates"
# set up parameters
params = {
    "page": 1,
    "per_page": 10,
    "from": "2024-06-01",
    "to": "2024-07-01",
}

# querystring = {"name":"italy","format":"json"}
#
# headers = {
#     "x-rapidapi-key": "c2809bb339mshd4c230066b81a5cp168e6ejsnb0f55d5d2fce",
#     "x-rapidapi-host": "covid-19-data.p.rapidapi.com"
# }

# response = requests.get(base_url, params=params)
# if response.status_code == 200:
#     python_obj = response.json()
#     print(type(python_obj['data']['payload']))
#     entry = python_obj['data']['payload'][3]
#     print(f"entry type: {type(entry)}")
#     print(f"rates type: {type(entry['rates'])}")
#     if isinstance(entry['rates'], list):
#         for items in entry['rates']:
#             # print(items)
#             name = items['currency']['name']
#             currency_code = items['currency']['iso3']
#             unit = items['currency']['unit']
#             buy = items['buy']
#             sell = items['sell']
#             print(f"Currency: {name}, Code: {currency_code}, Unit: {unit} Buy: {buy}, Sell: {sell}")
#
#     # string_obj = json.dumps(python_obj, indent=3)
#     # print(string_obj)
# else:
#     print(f"Error: {response.status_code}")

# ---------------------------------
# to print the elements of lists
# for obj in python_obj:
#     print(obj['id'], obj['title'])
#     print(f"Id:{obj['id']} and Title: {obj['title']} ")


# ----------------working with pandas
import pandas as pd
from geopy.geocoders import Nominatim

df1 = pd.DataFrame([[2.5, 5], [4, 20], [3, 18]], columns=["rate", "price"])
print(df1.price.mean())

# loading csv file
# df2 = pd.read_csv('country.csv')
# index = df2.set_index('Name')
# print(index)

# loading json file
# df3 = pd.read_json('supermarkets.json')
# df3.set_index('ID', inplace=True)
# the inplace=True, means the original dataframe will be modified, rather than creating a new one
# print(f"using loc: {dict(df3.loc[4:, 'Name'])}")
# Used as: -------------- df.iloc[row_indices, column_indices]
# print(f"using iloc: {df3.iloc[1:3, 1:4]}")

# Deleting the rows and columns
# df3 = df3.drop(df3.index[0:1], axis=0)
# print(df3, "\n\n")
#
# df3_columns = df3.drop(df3.columns[1:3], axis=1)
# print(df3_columns, "\n\n\n")

# The second argument 0 (or alternatively, you could use axis=0) specifies that we're dropping a row.
# If it were 1 (or axis=1), it would drop a column.
# print("columns: ",  df3.columns, "\n index: ", df3.index)

# add columns
# df3['Continent'] = ["North America", "North America", "Asia", "Antarctica", "Asia"]
# can alternatively also be done as below, to add five times
# df3['Continent'] = df3.shape[0] * [North America]
# print(df3)

# Using geocoders
# A geocoding service that converts addresses into latitude and longitude coordinates and vice versa.
nom = Nominatim(user_agent="my_geolocator")
n = nom.geocode("Imadol, Lalitpur, Nepal")
print(f"Data: {n} \nLat: {n.latitude}, Lon: {n.longitude}")

# using the csv file to geolocate
df4 = pd.read_json('supermarkets.json')

# to modify 'Address' column
df4['Address'] = df4['Address'] + ',' + df4['City'] + ',' + df4['State'] + ',' + df4['Country']

# to add "Coordinates" column by applying nom.geocode to "Address" column's data
df4["Coordinates"] = df4["Address"].apply(nom.geocode)

# to add latitude and longitude columns using lambda function
df4["Lat"] = df4["Coordinates"].apply(lambda x: x.latitude if x is not None else None)
df4["Long"] = df4["Coordinates"].apply(lambda x: x.longitude if x is not None else None)

print(df4)
# print(df4.Coordinates[1].latitude, df4.Coordinates[1].longitude)
