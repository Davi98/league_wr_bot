import time
import re
from log import log
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import json
from webdriver_manager.chrome import ChromeDriverManager

class Browser:

    def __init__(self):
        self.options = Options()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument("--window-size=960, 540")
        self.options.add_argument('--disable-extensions')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=self.options)
        self.session_id = self.driver.session_id
        self.command_executor_url = self.driver.command_executor._url
    

    def __del__(self):
        if hasattr(self, 'driver') and self.driver is not None:
            self.driver.quit()

