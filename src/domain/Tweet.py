from log import log


class Tweet:
    
    def __init__(self,api):
        
        self.api = api


    def create_first_tweet(self,champion):
        log().debug("Creating the first champion tweet:")
        first_text = f"Champions stats in {champion.role} lane at diamond plus solo queue in {champion.region} server at {champion.patch} patch:\n\n\n"
        second_text,image = self.create_champ_tweet_with_image(champion)
        
        tweet = first_text + second_text

        return tweet,image

    def create_champ_tweet_with_image(self,champion):
        log().debug(f"Creating tweet with image from  the {champion.name} in {champion.rank}º rank at {champion.role} lane")
        text = f"{champion.name} is the rank: {champion.rank}º at {champion.role} lane with {champion.win_rate} win rate, {champion.pick_rate} pick rate and {champion.ban_rate} ban rate in {champion.num_matches} matches"
        image = self.search_image(champion.name)
        return text, image

    def create_champ_tweet(self,champion):
        log().debug(f"Creating tweet from  the {champion.name} in {champion.rank}º rank at {champion.role} lane")
        text = f"{champion.name} is the rank: {champion.rank}º at {champion.role} lane with {champion.win_rate} win rate, {champion.pick_rate} pick rate and {champion.ban_rate} ban rate in {champion.num_matches} matches"

        return text
    
    
    def search_image(self,champion_name):
        champion_name = champion_name.replace(" ", "")
        champion_name = champion_name.replace("'", "")
        filename = f"./img/{champion_name}.jpg"
        media_ids = []
        res = self.api.media_upload(filename)
        media_ids.append(res.media_id)
        return media_ids



    def post(self,role_tier_list):
        try:
            for i in range(len(role_tier_list)):
                if i == 0:
                    status,image = self.create_first_tweet(role_tier_list[i])
                    post = self.api.update_status(status=status,media_ids=image)
                elif 0<i<=9:
                    status,image = self.create_champ_tweet_with_image(role_tier_list[i])
                    post = self.api.update_status(status=status,media_ids=image,in_reply_to_status_id = post._json['id'])
                else:
                    status =  self.create_champ_tweet(role_tier_list[i])
                    post = self.api.update_status(status=status,in_reply_to_status_id = post._json['id'])

        except Exception as err:
            log().error(f"Error posting in twitter : {type(err)} > {err}")


