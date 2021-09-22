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
            time.sleep(5)
             
            
            
            log().info("Starting crawling brazilian server winrates")
            browser.driver.get(url)


            time.sleep(5)
            self.accept_cookies(browser)
            time.sleep(5) 
            names = browser.driver.find_elements_by_xpath("//a[@class='champion-played gtm-tierlist-champion']//strong")
            name = browser.driver.find_element_by_xpath("//a[@class='champion-played gtm-tierlist-champion']//strong")
            print(name.get_attribute("innerText"))
            print(len(names))
            print(names[0].get_attribute("innerText"))
        except Exception as err:
            log().error(f"Error crawling : {type(err)} > {err}")


    def accept_cookies(self,browser):
        actions = ActionChains(browser.driver)     
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
