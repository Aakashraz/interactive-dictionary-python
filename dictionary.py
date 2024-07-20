import json
import requests
from difflib import get_close_matches


# function to find the matching word
def find(word):
    if word in data:
        return data[word]
    # to check if there are other words that matches with words in the data.json file,
    # data.keys() return the list(type: dict_keys) of keys of the key:value pairs of the dictionary
    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = get_close_matches(word, data.keys())[0]
        replacement_word = input("Did you mean %s instead? \n Enter Y if yes, or N if no: " % close_match )
        if replacement_word.lower() == 'y':
            return data[close_match]
        elif replacement_word.lower() == 'n':
            return "The word doesn't exist. Please double check your spelling and try again."
        else:
            return "We can understand what you meant."
    else:
        return "No such word found!"


with open('data.json', 'r') as json_file:
    data = json.load(json_file)
    search = input("Enter a word: ")
    print(find(search.lower()))

# url = "https://covid-19-data.p.rapidapi.com/country/code"
#
# querystring = {"format": "json", "code": "np"}
#
# headers = {
#     "x-rapidapi-key": "c2809bb339mshd4c230066b81a5cp168e6ejsnb0f55d5d2fce",
#     "x-rapidapi-host": "covid-19-data.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# response_data = response.json()
# obj = json.dumps(response_data, indent=2)
# print(type(obj))
# print(obj)
