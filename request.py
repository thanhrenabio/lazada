import requests
import json
url = 'https://api.lazada.vn/rest'
appkey = 109972
appSecret ='z8xnlsik8ZD4ahqzgoX8hwSmx3B4kCMh'


# webhook_url = 'https://api.unitekpharma.com/webhook'
# data = {
# 	'name': 'Thanh Nguyen',
# 	'age': 32
# }
# r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type':'application/json'})

client = lazop.LazopClient(url, appkey ,appSecret)
request = lazop.LazopRequest('/finance/payout/status/get','GET')
request.add_api_param('created_after', '2022-06-01')
response = client.execute(request, access_token)
print(response.type)
print(response.body)