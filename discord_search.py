import requests
import json
import os

def retrieve_messages(channelid):
    headers={
        'authorization':os.environ.get('DISCORD_AUTH')
    }
    r=requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers, params={'limit':'100'})
    jsonn = json.loads(r.text)
    count=0
    for value in jsonn:
        count+=1
        print(value['content'], '\n')
    print(count)

channel_id='968427811226419211'
a=1
