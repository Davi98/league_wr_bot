import concurrent.futures
from src.browser.Browser import Browser
from src.domain.Spider import Spider
import src.utils.environment as env
from log import log
from src.domain.UrlFactory import UrlFactory
from src.domain.TierList import TierList



spider = Spider()
browser = Browser()
url = UrlFactory(env.region).link_selector()
champions = spider.crawl(url,browser)
top_tier_list,jungle_tier_list,mid_tier_list,bot_tier_list,sup_tier_list = TierList().sort_by_lane(champions)

for i in range(len(top_tier_list)):
    print(top_tier_list[i].__dict__)

# for i in len(jungle_tier_list):
#     print(jungle_tier_list[i].__dict__)

# for i in len(mid_tier_list):
#     print(mid_tier_list[i].__dict__)

# for i in len(bot_tier_list):
#     print(bot_tier_list[i].__dict__)

# for i in len(sup_tier_list):
#     print(sup_tier_list[i].__dict__)

