import requests
import json

url = requests.get('https://rbx.jmk.gg/getOnline')
data = json.loads(url.text)
roles = {'4199740': 'video star', 'dev': 'developer', '1200769': 'Administrator'}


def find_online():
    for groupId in data:
        status = data[groupId]
        for keys in status:
            if keys and keys['placeId'] == 6674394294:
                for i in roles:
                    if i in groupId:
                        role = roles[i]
                        print(role)


find_online()
