from src.browser.Browser import Browser
from src.domain.Spider import Spider
from log import log
from src.domain.UrlFactory import UrlFactory
from src.domain.TierList import TierList
from src.domain.Tweet import Tweet
from src.infra.twitter.Twitter import Twitter
from dotenv import load_dotenv
import time
import os

load_dotenv()
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")



api = Twitter(consumer_key,consumer_secret,access_token,access_token_secret).auth()



spider = Spider()
browser = Browser()
tweet = Tweet(api)
url = UrlFactory(os.environ.get("REGION")).link_selector()

champions = spider.crawl(url,browser)
top_tier_list,jungle_tier_list,mid_tier_list,bot_tier_list,sup_tier_list = TierList().sort_by_lane(champions)



tweet.post(top_tier_list)
time.sleep(10)
tweet.post(jungle_tier_list)
time.sleep(10)
tweet.post(mid_tier_list)
time.sleep(10)
tweet.post(bot_tier_list)
time.sleep(10)
tweet.post(sup_tier_list)



