from src.browser.Browser import Browser
from src.domain.Spider import Spider
import src.utils.environment as env
from log import log
from src.domain.UrlFactory import UrlFactory
from src.domain.TierList import TierList
from src.infra.twitter.Twitter import Twitter
import tweepy as tw
 

consumer_key = 'OYvAoUGa8l1pXUj7Xljme89WO'
consumer_secret = 'KT2CbZwYIkijDufRjPc4BJY9CwNEIeBCsJg97IpzqN6FUSdksf'
access_token = '1438506500570292229-5KBubRYZ04MsyDSWf4LXPEBe0cVmFc'
access_token_secret = 'wKkMD4JnKlH0FWWN6V6CwOWSObBWWWs04pzHaKMOwiMx6'
i = 0
api = Twitter(consumer_key,consumer_secret,access_token,access_token_secret).auth()


filenames = ['./img/Aatrox.jpg', './img/Ahri.jpg','./img/Ahri.jpg','./img/Ahri.jpg']
media_ids = []
for filename in filenames:
     res = api.media_upload(filename)
     media_ids.append(res.media_id)

# Tweet with multiple images
api.update_status(status='many images!✨', media_ids=media_ids)

spider = Spider()
browser = Browser()
url = UrlFactory(env.region).link_selector()
champions = spider.crawl(url,browser)
top_tier_list,jungle_tier_list,mid_tier_list,bot_tier_list,sup_tier_list = TierList().sort_by_lane(champions)

for i in range(len(top_tier_list)):
    if i == 0:
        tweet = api.update_status(top_tier_list[i].__dict__)
    else:
        tweet = api.update_status(top_tier_list[i].__dict__,in_reply_to_status_id = tweet._json['id'])




