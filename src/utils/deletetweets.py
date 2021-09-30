from src.infra.twitter.Twitter import Twitter
import tweepy as tw
from dotenv import load_dotenv
import os

load_dotenv()
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")



api = Twitter(consumer_key,consumer_secret,access_token,access_token_secret).auth()

for status in tw.Cursor(api.user_timeline).items():
    api.destroy_status(status.id)

# python -m src.utils.deletetweets