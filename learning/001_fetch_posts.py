import requests
import json
from pprint import pprint 

handle           = 'lain@pleroma.soykaf.com'
# handle           = 'JoannaMasel@fediscience.org'
username, domain = handle.split('@')

wf_url = 'https://{}/.well-known/webfinger'.format(domain)
wf_par = {'resource': 'acct:{}'.format(handle)}
wf_hdr = {'Accept': 'application/jrd+json'}

# Perform the request
wf_resp = requests.get(wf_url, headers=wf_hdr, params=wf_par).json()

pprint(wf_resp)

user_url = wf_resp["links"][0]["href"]
print(user_url)
as_header = {'Accept': 'application/ld+json; profile="https://www.w3.org/ns/activitystreams"'}
user_json = requests.get(user_url, headers=as_header).json()

print("\n\n")
pprint(user_json)

print("\n\n======\n\n")

as_header = {'Accept': 'application/ld+json; profile="https://www.w3.org/ns/activitystreams"'}
feed_url  = user_json['outbox']
feed = requests.get(feed_url, headers=as_header).json()
pprint(feed)
feed = requests.get(feed["first"], headers=as_header).json()
pprint(feed)