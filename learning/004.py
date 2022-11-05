import requests
import json

response = requests.get("https://mastodon.kindred.at/api/v1/timelines/public")
statuses = json.loads(response.text) # this converts the json to a python list of dictionary
assert statuses[0]["visibility"] == "public" # we are reading a public timeline
print(statuses[0]["content"]) # this prints the status text