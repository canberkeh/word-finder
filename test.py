import json
import requests
headers = {'content-type': 'application/json'}
post_data = {'length' : "5", "word": "s   m" }

# response = requests.post("http://word-finder-get-words.herokuapp.com/word_finder/get_words", data=json.dumps(post_data), headers=headers, auth=("word_finder", "wordie1993@"))
response = requests.post("http://localhost:5000/word_finder/get_words", data=json.dumps(post_data), headers=headers, auth=("word_finder", "wordie1993@"))

print(response.content)