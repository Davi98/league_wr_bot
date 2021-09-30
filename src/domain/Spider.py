from src.browser.Browser import Browser
from src.domain.Champion import Champion
from log import log
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from itertools import chain
from itertools import zip_longest

class Spider:
    

    def crawl(self,url,browser):
        try:
            index = 0
            champions = []
            
            
            time.sleep(5)
            
            log().info(f"Starting crawling in {url.region} region at link:{url.link}")
            
            
            browser.driver.get(url.link)
            time.sleep(15)
            
            log().debug("Scrolling down page to access more champions in the list")
            self.scroll_down(browser)


            log().debug("Crawling patch number")
            patch = browser.driver.find_element_by_xpath("//div[@class='header-patch media-query media-query_TABLET__DESKTOP_LARGE']").text
            patch = (patch.replace("Patch ",""))


            log().debug("Crawling champions infos")
            names = browser.driver.find_elements_by_xpath("//a[@class='champion-played gtm-tierlist-champion']//strong")
            roles = browser.driver.find_elements_by_xpath("//img[@class='tier-list-role']")
            
            win_rates_odd = browser.driver.find_elements_by_xpath("//div[@class='rt-td winrate sorted is-in-odd-row']//span//b")
            win_rates_even = browser.driver.find_elements_by_xpath("//div[@class='rt-td winrate sorted']//span//b")
            win_rates = self.join_odd_even_array(win_rates_odd,win_rates_even)
            
            pick_rates_odd = browser.driver.find_elements_by_xpath("//div[@class='rt-td pickrate is-in-odd-row']//span")
            pick_rates_even = browser.driver.find_elements_by_xpath("//div[@class='rt-td pickrate']//span")
            pick_rates = self.join_odd_even_array(pick_rates_odd,pick_rates_even)
            
            ban_rates_odd = browser.driver.find_elements_by_xpath("//div[@class='rt-td banrate is-in-odd-row']//span")
            ban_rates_even = browser.driver.find_elements_by_xpath("//div[@class='rt-td banrate']//span")
            ban_rates = self.join_odd_even_array(ban_rates_odd,ban_rates_even)

            num_matches_odd = browser.driver.find_elements_by_xpath("//div[@class='rt-td matches is-in-odd-row']//span")
            num_matches_even = browser.driver.find_elements_by_xpath("//div[@class='rt-td matches']//span")
            num_matches = self.join_odd_even_array(num_matches_odd,num_matches_even)
            
           
            
            

            for index in range(len(names)):
                log().debug("Creating champion objects:")
                champions.append(Champion(index+1,(roles[index].get_attribute("alt")).upper(),names[index].get_attribute("innerText"),win_rates[index].get_attribute("innerText"),pick_rates[index].get_attribute("innerText"),ban_rates[index].get_attribute("innerText"),num_matches[index].get_attribute("innerText"),url.region,patch))
                log().debug(f"This object of a champion rates was created: {champions[index].__dict__}")

            return champions


        except Exception as err:
            log().error(f"Error crawling : {type(err)} > {err}")


    def join_odd_even_array(self,odd_array,even_array):
        array = []
        array = list(filter(lambda odd_array: odd_array != '', chain.from_iterable(zip_longest(odd_array, even_array, fillvalue = ''))))
        return array

    def scroll_down(self,browser):
        for i in range(5):
            browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

    def accept_cookies(self,browser):
        actions = ActionChains(browser.driver)     
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        time.sleep(5) 
