
from utils.base_test import BaseTest

class TestCheckout(BaseTest):
    def test_checkout_flow(self):
        d = self.driver
        d.find_element("id", "user-name").send_keys("standard_user")
        d.find_element("id", "password").send_keys("secret_sauce")
        d.find_element("id", "login-button").click()
        d.find_element("id", "add-to-cart-sauce-labs-backpack").click()
        d.find_element("class name", "shopping_cart_link").click()
        d.find_element("id", "checkout").click()
        d.find_element("id", "first-name").send_keys("John")
        d.find_element("id", "last-name").send_keys("Doe")
        d.find_element("id", "postal-code").send_keys("400001")
        d.find_element("id", "continue").click()
        d.find_element("id", "finish").click()
        success_msg = d.find_element("class name", "complete-header").text
        self.assertEqual(success_msg, "THANK YOU FOR YOUR ORDER")
