from src.infra.twitter.Twitter import Twitter
import tweepy as tw
 

consumer_key = 'OYvAoUGa8l1pXUj7Xljme89WO'
consumer_secret = 'KT2CbZwYIkijDufRjPc4BJY9CwNEIeBCsJg97IpzqN6FUSdksf'
access_token = '1438506500570292229-5KBubRYZ04MsyDSWf4LXPEBe0cVmFc'
access_token_secret = 'wKkMD4JnKlH0FWWN6V6CwOWSObBWWWs04pzHaKMOwiMx6'


api = Twitter(consumer_key,consumer_secret,access_token,access_token_secret).auth()

for status in tw.Cursor(api.user_timeline).items():
    api.destroy_status(status.id)

