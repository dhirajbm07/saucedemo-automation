
from utils.base_test import BaseTest

class TestLogin(BaseTest):
    def test_valid_login(self):
        self.driver.find_element("id", "user-name").send_keys("standard_user")
        self.driver.find_element("id", "password").send_keys("secret_sauce")
        self.driver.find_element("id", "login-button").click()
        self.assertIn("inventory", self.driver.current_url)
