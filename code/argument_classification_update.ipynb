import json
import requests
import os
from tqdm import tqdm
import argparse
from datetime import datetime


"""
Reads documents with split sentences, classifies them into pro-/con-/non-arguments, and writes out arguments and their stance information.
"""
userID = "fill in your ID"
APIkey = "fill in your key"
path = '/Users/wanglian/Desktop/filing'


def get_doc_list(path):
    if os.path.isfile(path+"../processed_docs.txt"):
        with open(path+"../processed_docs.txt", "r") as in_f:
            processed_docs = in_f.readlines()
            if len(processed_docs) == 0:
                return sorted(os.listdir(path))
            processed_docs = processed_docs[0].split(",")
            if processed_docs[-1] == "":
                processed_docs = processed_docs[:-1]
            processed_docs = set(processed_docs)
            all_docs = set(sorted(os.listdir(path)))
            return sorted(all_docs.difference(processed_docs))
    else:
        return sorted(os.listdir(path))
path = '/Users/wanglian/Desktop/filing'
print(get_doc_list(path))
a = []
for i in range(1,len(get_doc_list(path))):  
    a.append(path + '/' + get_doc_list(path)[i])

for j in range(len(a)):
    
    with open(a[j]) as f:
        currFiling = " ".join(f.readlines())
    payload = {
    "topic": "technology",
    "text": currFiling,
    "predictStance": True,
    "computeAttention": True,
    "showOnlyArguments": False,
    "userID": userID,
    "apiKey": APIkey
    }

json_dict = requests.post("https://api.argumentsearch.com/en/classify", timeout=300, data=json.dumps(payload), headers={'Content-Type': 'application/json'}).json()

print(json_dict)

print(a)






    

    
     




