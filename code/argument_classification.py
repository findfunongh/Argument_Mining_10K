import json
import requests
import os
from datetime import datetime
from credentials import userID, APIkey


with open("data/Filing_1.txt") as f:
    currFiling = " ".join(f.readlines())



payload = {
    "topic": "tempo limit",
    "text": currFiling,
    "predictStance": True,
    "computeAttention": True,
    "showOnlyArguments": False,
    "userID": userID,
    "apiKey": APIkey 
    }

json_dict = requests.post("https://api.argumentsearch.com/en/classify", timeout=300, data=json.dumps(payload), headers={'Content-Type': 'application/json'}).json()

print(json_dict)

