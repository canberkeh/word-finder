import json
import requests
headers = {'content-type': 'application/json'}
post_data = {"exclude": [
    "c",
    "z"
  ],
  "include": [
    "a",
    "s"
  ],'length' : "5", "word": "s   m", "language": "tr"}

response = requests.post("http://word-finder-get-words.herokuapp.com/word_finder/get_words", data=json.dumps(post_data), headers=headers, auth=("word_finder", "youshallnotpass"))

print(response.content)

# response = requests.post("http://word-finder-get-words.herokuapp.com/word_finder/get_words", data=json.dumps(post_data), headers=headers, auth=("word_finder", "wordie1993@"))
