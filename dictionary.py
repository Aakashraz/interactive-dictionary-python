import json


# function to find the matching word
def find(word):
    if word in data:
        return data[word]
    else:
        return "No such word found!"


with open('data.json', 'r') as json_file:
    data = json.load(json_file)
    search = input("Enter a word: ")
    print(find(search.lower()))