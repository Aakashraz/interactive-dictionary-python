import json
import requests

# function to find the matching word
# def find(word):
#     if word in data:
#         return data[word]
#     else:
#         return "No such word found!"
#
#
# with open('data.json', 'r') as json_file:
#     data = json.load(json_file)
#     search = input("Enter a word: ")
#     print(find(search.lower()))\


url = "https://covid-19-data.p.rapidapi.com/country/code"

querystring = {"format": "json", "code": "np"}

headers = {
    "x-rapidapi-key": "c2809bb339mshd4c230066b81a5cp168e6ejsnb0f55d5d2fce",
    "x-rapidapi-host": "covid-19-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()
obj = json.dumps(data, indent=2)
print(type(obj))

print(obj)