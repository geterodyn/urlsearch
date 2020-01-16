import requests

def word_count(url, word):
    response = requests.get(url)
    words_list = response.text.split()
    return words_list.count(word)


