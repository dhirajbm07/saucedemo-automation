
from selenium import webdriver
import unittest

class BaseTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Optional for online/cloud
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
