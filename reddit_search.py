import requests
import praw
import os
import pandas as pd
from sqlalchemy import create_engine

CLIENT_ID=os.environ.get('REDDIT_CLIENT_ID')
SECRET_KEY=os.environ.get('REDDIT_SECRET_KEY')
pw = os.environ.get('REDDIT_PW')
username = os.environ.get('REDDIT_USERNAME')

#Setting up access to the Reddit API
auth=requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

data={
    'grant_type': 'password',
    'username': username,
    'password': pw
}

headers = {'User-Agent':'MyAPI/0.0.1'}


res=requests.post('https://www.reddit.com/api/v1/access_token',
                  auth=auth, data=data, headers=headers)

TOKEN=res.json()['access_token']

headers['Authorization']=f'bearer {TOKEN}'

reddit=praw.Reddit(user_agent="Get Comments",client_id=CLIENT_ID,client_secret=SECRET_KEY)

hotpost=requests.get('https://oauth.reddit.com/r/CryptoCurrency/search/?q=Bitcoin&sort=new',
                 headers=headers, params={'restrict_sr':'1','limit':'10'}).json()

for post in hotpost['data']['children']:
    print(post['data']['title'])

df = pd.DataFrame()

for post in hotpost['data']['children']:
    submission = reddit.submission(id=post['data']['id'])
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        df=df._append({
            'subreddit':post['data']['subreddit'],
            'title':post['data']['title'],
            'selftext':post['data']['selftext'],
            'upvote_ratio':post['data']['upvote_ratio'],
            'ups':post['data']['ups'],
            'downs':post['data']['downs'],
            'score':post['data']['score'],
            'id':post['data']['id'],
            'name':post['data']['name'],
            'comment':comment.body,
            'comment_ups':comment.ups,
            'comment_downs':comment.downs
            }, ignore_index=True)

engine=create_engine('sqlite:///data/reddit_comments.db',echo=True)
sqlite_connection=engine.connect()
sqlite_table='reddit_comments'
df.to_sql(sqlite_table,sqlite_connection, if_exists='fail')
sqlite_connection.close()

print(df)
print(post['kind'])
print(df['subreddit'])

#print(post['data'].keys())
