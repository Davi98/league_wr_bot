from src.domain.Url import Url 

class UrlFactory():
    def __init__(self,region):
        self.region = region.upper()
        self.links = dict(BR="https://u.gg/lol/tier-list?rank=diamond_plus&region=br1",
                     NA="https://u.gg/lol/tier-list?rank=diamond_plus&region=na1",
                     KR="https://u.gg/lol/tier-list?rank=diamond_plus&region=kr",
                     EUW = "https://u.gg/lol/tier-list?rank=diamond_plus&region=euw1",
                     WORLD =  "https://u.gg/lol/tier-list?rank=diamond_plus")
        

    def link_selector(self):
        if self.region in self.links:
            return Url(self.links.get(self.region),self.region)
        else:
            return Url(self.links.get("WORLD"),"WORLD")


            
        
        