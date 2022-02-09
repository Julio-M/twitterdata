import tweepy
import pandas as pd
import json
import csv

# Your app's bearer token can be found under the Authentication Tokens section
# of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
bearer_token = ""

# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
consumer_key = ""
consumer_secret = ""

# Your account's (the app owner's account's) access token and secret for your
# app can be found under the Authentication Tokens section of the
# Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
access_token = ""
access_token_secret = ""

# You can authenticate as your app with just your bearer token
client = tweepy.Client(bearer_token=bearer_token)

response = client.search_recent_tweets("bitcoin",max_results=10)
# The method returns a Response object, a named tuple with data, includes,
# errors, and meta fields
print(response.meta)

# In this case, the data field of the Response returned is a list of Tweet
# objects
tweets = response.data

file = "./tweet.csv"
with open(file, 'w',) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id','tweet_id', 'text'])
    id=0
    for tweet in tweets:
        id+=1
        writer.writerow([id,tweet.id, tweet.text])


