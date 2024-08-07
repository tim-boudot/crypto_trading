import tweepy
import os

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object
api = tweepy.API(auth)

# Example: Fetch 5 tweets from a user's timeline
#user_tweets = api.user_timeline(screen_name='Cyruslevirous', count=5)

# list of screen_names
screen_names = ["Cyruslevirous"]

# getting the users by screen_names
users = api.lookup_users(screen_names = screen_names)

# printing the user details
for user in users:
    print("The id is : " + str(user.id))
    print("The screen name is : " + user.screen_name, end = "\n\n")

# Print the tweetsfor tweet in user_tweets:
#print(tweet.text)
