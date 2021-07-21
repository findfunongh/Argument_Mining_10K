import json
import requests
import os
from tqdm import tqdm
from datetime import datetime


userID = "uvsbmgi1"
APIkey = "o2N7OBExiLAAUo5xwM2LuGhHHRCQs+E1"


"""
Based on sentence

#topic = "Liquidity"
#sents_to_send = ["We believe that cash flows generated from operations and our cash, cash equivalents, and marketable securities balances, as well as our borrowing arrangements, will be sufficient to meet our anticipated operating cash needs for at least the next twelve months."]

payload = {"topic": topic,
"showOnlyArguments": False,
"computeAttention": False,
"sortBy": "none",
"predictStance": True,
"sentences": sents_to_send,
"userID": userID,
"apiKey": APIkey
}
"""


"""
payload = {
    "topic": "Brexit",
    "targetUrl": "https://www.washingtonpost.com/world/2018/12/14/is-theresa-may-bad-negotiator-or-is-brexit-just-an-impossible-proposition-answer-yes",
    "predictStance": True,
    "computeAttention": True,
    "showOnlyArguments": False,
    "userID": userID,
    "apiKey": APIkey
    }
"""




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