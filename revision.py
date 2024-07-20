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


# using date and time
import datetime
import time

first = []
for i in range(5):
    # now().strftime will format the time accordingly
    first.append(datetime.datetime.now().strftime("%Y %b %d %I:%M %p"))
    time.sleep(1)
for i in first:
    print(i)  # to print in new lines

# json api call
# url = "https://jsonplaceholder.typicode.com/users/1/posts"

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

response = requests.get(base_url, params=params)
if response.status_code == 200:
    python_obj = response.json()
    print(type(python_obj['data']['payload']))
    entry = python_obj['data']['payload'][3]
    print(f"entry type: {type(entry)}")
    print(f"rates type: {type(entry['rates'])}")
    if isinstance(entry['rates'], list):
        for items in entry['rates']:
            # print(items)
            name = items['currency']['name']
            currency_code = items['currency']['iso3']
            unit = items['currency']['unit']
            buy = items['buy']
            sell = items['sell']
            print(f"Currency: {name}, Code: {currency_code}, Unit: {unit} Buy: {buy}, Sell: {sell}")

    # string_obj = json.dumps(python_obj, indent=3)
    # print(string_obj)
else:
    print(f"Error: {response.status_code}")

# to print the elements of lists
# for obj in python_obj:
#     print(obj['id'], obj['title'])
#     print(f"Id:{obj['id']} and Title: {obj['title']} ")
