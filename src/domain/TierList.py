from log import log

class TierList():

    def sort_by_lane(self,champions):
        log().debug("Sorting champions by lanes")
        top_list = []
        jungle_list = []
        mid_list = []
        bot_list = []
        sup_list = []
        ranks = [1,1,1,1,1]
        
        for champ in champions:
            if champ.role == "TOP":
                champ.rank = ranks[0]
                top_list.append(champ)
                ranks[0] +=1
            elif champ.role == "JUNGLE":
                champ.rank = ranks[1]
                jungle_list.append(champ)
                ranks[1] +=1
            elif champ.role == "MID":
                champ.rank = ranks[2]
                mid_list.append(champ)
                ranks[2] +=1
            elif champ.role == "ADC":
                champ.rank = ranks[3]
                champ.role = "BOT"
                bot_list.append(champ)
                ranks[3] +=1
            elif champ.role == "SUPP":
                champ.rank = ranks[4]
                champ.role = "SUP"
                sup_list.append(champ)
                ranks[4] +=1
    
        return top_list,jungle_list,mid_list,bot_list,sup_list