import concurrent.futures
import time
from src.browser.Browser import Browser
from src.Spider import Spider
import src.utils.environment as env
from log import log
from src.schema.Url import Url
from src.utils.links import links
from src.schema.Champion import Champion

browser = Browser(env.tor_port)
url = Url(links[0])
spider = Spider()
spider.crawl(url.link,browser)



# drivers = [Browser(env.tor_port) for _ in range(len(mini_docs))]
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(kavakPrice.price_car, mini_docs, drivers)