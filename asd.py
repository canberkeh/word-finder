import json
import requests
headers = {'content-type': 'application/json'}
post_data = {'length' : "5", "word": "s   m" }

response = requests.post("https://word-finder-get-words.herokuapp.com/word_finder/get_word", data=json.dumps(post_data), headers=headers, auth=("word_finder", "wordie1993@"))
print(response.content.encode('utf-8'))