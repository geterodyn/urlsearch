import requests

def word_count(url, word):
    try:
        response = requests.get(url)
        words_list = [x.lower() for x in response.text.split()]
        return words_list.count(word.lower())
    except requests.exceptions.RequestException:
        return 'unavailable'


