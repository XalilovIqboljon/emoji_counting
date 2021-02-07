import requests
from pprint import pprint


token = "1679454024:AAEs98zOJvEYgdYwbZgFaJQQMSsBHFWHdnc"
def getUpdates():
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    r=requests.get(url).json()
    data=r['result']
    return data
data=getUpdates()

dislike='👎'
like='👍🏽'
dict1={}

for i in data:
    message=i['message']
    text=message['text']
    if text==like:
        print(like)
    if text==dislike:
        print(dislike)
