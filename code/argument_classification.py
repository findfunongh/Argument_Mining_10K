import json
import requests
import os
from datetime import datetime
from credentials import userID, APIkey




'''
payload = {
    "topic": "Brexit",
    "text": ,
    "predictStance": True,
    "computeAttention": True,
    "showOnlyArguments": False,
    "userID": userID,
    "apiKey": APIkey
    }







json_dict = requests.post("https://api.argumentsearch.com/en/classify", timeout=300, data=json.dumps(payload), headers={'Content-Type': 'application/json'}).json()

print(json_dict)

'''