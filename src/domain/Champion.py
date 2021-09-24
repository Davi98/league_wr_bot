from datetime import datetime,date

class Champion:
    def __init__(self,rank,role,name,win_rate,pick_rate,ban_rate,num_matches,region,patch):

        self.rank = rank
        self.role = role
        self.name = name
        self.win_rate = win_rate
        self.pick_rate = pick_rate
        self.ban_rate = ban_rate
        self.num_matches = num_matches
        self.region = region
        self.patch = patch
        self.date = datetime.utcnow()


