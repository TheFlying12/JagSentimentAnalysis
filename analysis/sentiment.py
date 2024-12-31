import os 
from dotenv import load_dotenv
import tweepy
import pandas as pd

load_dotenv()


# Replace with your keys
BEARER_TOKEN = os.getenv(BEARER_TOKEN)


# Setup Tweepy Client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Function to fetch tweets
def fetch_tweets(query, max_results=100):
    response = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=['created_at', 'text', 'author_id'])
    tweets = [{'text': tweet.text, 'created_at': tweet.created_at, 'author_id': tweet.author_id} for tweet in response.data]
    return pd.DataFrame(tweets)

# Fetch tweets
query = '"Jaguar rebrand" OR #JaguarRebrand -is:retweet lang:en'
tweets_df = fetch_tweets(query, max_results=100)
print(tweets_df.head())
