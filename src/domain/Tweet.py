class Tweet:
    
    def __init__(self,api):
        
        self.api = api


    def create_first_tweet(self,champion):
        first_text = f"Champions stats in diamond plus solo queue at {champion.region} server in patch {champion.patch}:\n\n\n"
        second_text,image = self.create_champ_tweet_with_image(champion)
        
        tweet = first_text + second_text

        return tweet,image

    def create_champ_tweet_with_image(self,champion):
        text = f"{champion.name} is the rank: {champion.rank}º at {champion.role} lane with {champion.win_rate} win rate, {champion.pick_rate} pick rate and {champion.ban_rate} ban rate in {champion.num_matches} matches"
        image = self.search_image(champion.name)
        return text, image

    def create_champ_tweet(self,champion):
        text = f"{champion.name} is the rank: {champion.rank}º at {champion.role} lane with {champion.win_rate} win rate, {champion.pick_rate} pick rate and {champion.ban_rate} ban rate in {champion.num_matches} matches"

        return text
    
    
    def search_image(self,champion_name):
        champion_name = champion_name.replace(" ", "")
        print(champion_name)
        image = f"./img/{champion_name}.jpg"
        return image



    def post(self,role_tier_list):
        for i in range(len(role_tier_list)):
            if i == 0:
                status,image = self.create_first_tweet(role_tier_list[i])
                post = self.api.update_with_media(image, status)
            elif 0<i<=9:
                status,image = self.create_champ_tweet_with_image(role_tier_list[i])
                post = self.api.update_with_media(image,status,in_reply_to_status_id = post._json['id'])
            else:
                status =  self.create_champ_tweet(role_tier_list[i])
                post = self.api.update_status(status,in_reply_to_status_id = post._json['id'])
