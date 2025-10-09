import json
import requests

request_link=f"https://d129b681-d2fb-4afc-8ff1-846b8cfc8942.mock.pstmn.io/orders/generate-order-reference"
response=requests.get(request_link)
print(response.status_code)
print(response.json())

post_link=f"https://d129b681-d2fb-4afc-8ff1-846b8cfc8942.mock.pstmn.io/orders/"
headers = {'Content-Type': 'application/json'}
data = {
    "orderRef": "f7032ebd-9ed2-4010-aab2-d7672f68e070",
    "customer": "Acme ",
    "sku": "2020/Iph/12/Blu",
    "deliveryDate": "2021-01-15"
}  
response = requests.post(post_link, headers=headers, json=data)
print(response.status_code)
print(response.json())