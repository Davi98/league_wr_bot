from src.browser.Browser import Browser
from src.schema.Champion import Champion
from log import log
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Spider:
    
    def __init__(self):

        self.mongo_repository = None





    
    def crawl(self,url,browser):
        try:
            index = 0
            even_index = 0
            odd_index = 0
            champions = []
            time.sleep(5)
             
            
            
            log().info("Starting crawling brazilian server winrates")
            browser.driver.get(url.link)
            time.sleep(10)
            

            self.scroll_down(browser)

            patch = browser.driver.find_element_by_xpath("//div[@class='header-patch media-query media-query_TABLET__DESKTOP_LARGE']").text

            patch = patch.replace("Patch","")

            names = browser.driver.find_elements_by_xpath("//a[@class='champion-played gtm-tierlist-champion']//strong")
            roles = browser.driver.find_elements_by_xpath("//img[@class='tier-list-role']")
            
            win_rates_odd = browser.driver.find_elements_by_xpath("//div[@class='rt-td winrate sorted is-in-odd-row']//span//b")
            win_rates_even = browser.driver.find_elements_by_xpath("//div[@class='rt-td winrate sorted']//span//b")
            
            pick_rates_odd = browser.driver.find_elements_by_xpath("//div[@class='rt-td pickrate is-in-odd-row']//span")
            pick_rates_even = browser.driver.find_elements_by_xpath("//div[@class='rt-td pickrate']//span")
            pick_rates = []
            
            ban_rates_odd = browser.driver.find_elements_by_xpath("//div[@class='rt-td banrate is-in-odd-row']//span")
            ban_rates_even = browser.driver.find_elements_by_xpath("//div[@class='rt-td banrate']//span")

            num_matches_odd = browser.driver.find_elements_by_xpath("//div[@class='rt-td matches is-in-odd-row']//span")
            num_matches_even = browser.driver.find_elements_by_xpath("//div[@class='rt-td matches']//span")


            for index in range(len(names)-1):
                if index == 0:


                    champions.append(champions.append(Champion(index+1,roles[index].get_attribute("alt"),names[index].get_attribute("innerText"),win_rates_odd[odd_index].get_attribute("innerText"),pick_rates_odd[odd_index].get_attribute("innerText"),ban_rates_odd[odd_index].get_attribute("innerText"),num_matches_odd[odd_index].get_attribute("innerText"),url.region,patch)))
                
                elif index%2 != 0:

                    champions.append(Champion(index+1,roles[index].get_attribute("alt"),names[index].get_attribute("innerText"),win_rates_odd[odd_index].get_attribute("innerText"),pick_rates_odd[odd_index].get_attribute("innerText"),ban_rates_odd[odd_index].get_attribute("innerText"),num_matches_odd[odd_index].get_attribute("innerText"),url.region,patch))
                    odd_index += 1
                elif index%2 == 0:

                    champions.append(Champion(index+1,roles[index].get_attribute("alt"),names[index].get_attribute("innerText"),win_rates_even[even_index].get_attribute("innerText"),pick_rates_even[even_index].get_attribute("innerText"),ban_rates_even[even_index].get_attribute("innerText"),num_matches_even[even_index].get_attribute("innerText"),url.region,patch))
                    even_index +=1
            

            return champions


        except Exception as err:
            log().error(f"Error crawling : {type(err)} > {err}")



    # def convert_webelement_string()    
            
    # def create_object()

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
