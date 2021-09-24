class Tweet:
    
        

    def create_first_tweet(self,champions):
        tweet = f"Champions stats in diamond plus solo queue at {champions[0].region} server in patch {champions[0].patch}:"

        
        return tweet

    def create_champ_tweet(self,champion):
        text = f"{champion.name} is the rank: {champion.rank}º at {champion.lane} lane with {champion.win_rate} win rate, {champion.pick_rate} pick rate {champion.ban_rate} ban rate {champion.num_matches} in matches"

        return text

    def search_image(self,champion_name):
        image = f"../../img/{champion_name}"
        return image