import tweepy as tw


class Twitter:
    
    def __init__(self,consumer_key,consumer_secret, access_token,access_token_secret):
        
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def auth(self):
        auth = tw.OAuthHandler(self.consumer_key,self.consumer_secret)
        auth.set_access_token(self.access_token,self.access_token_secret)
        api = tw.API(auth)
        return api

        
