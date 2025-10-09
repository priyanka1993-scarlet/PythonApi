""" 
Developer: aipython on [12-05-2021]
website: www.aipython.in

This program demonstrates the use case of  COWIN API (available in the public domain) to view the availability of 
vaccine type, Minimum eligible age, Available slot for a particular date and Pincode.

Check for COVID vaccine availability near you using Python | covid vaccine registration India | Python API
"""
import json
import requests
import pandas as pd


request_link = f"https://d129b681-d2fb-4afc-8ff1-846b8cfc8942.mock.pstmn.io/products/phone-sku"
response = requests.get(request_link)
value = response.json()
if response.status_code == 200:
    data=json.dumps(value,indent=4)
    with open('raw_JSON.json','w') as f:
        f.write(data)
print(response.status_code)    
print(value)

with open('raw_JSON.json') as f:
    data=json.load(f)
    rec=[]
    for i in data:
        rec.append(i)
df=pd.DataFrame(rec)
print(df.head())



