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


# json api call from yahoo finance
url = "https://covid-19-data.p.rapidapi.com/country"

querystring = {"name":"italy","format":"json"}

headers = {
    "x-rapidapi-key": "c2809bb339mshd4c230066b81a5cp168e6ejsnb0f55d5d2fce",
    "x-rapidapi-host": "covid-19-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()
obj = json.dumps(data, indent=4)
print(obj)
