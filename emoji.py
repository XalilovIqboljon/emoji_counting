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
a=0
b=0
for i in data:
    message=i['message']
    text=message['text']
    if text==like:
        a+=1
        dict1['like']=a
    if text==dislike:
        b+=1
        dict1['dislike']=b


print(dict1)