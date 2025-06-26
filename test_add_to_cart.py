
from utils.base_test import BaseTest

class TestAddToCart(BaseTest):
    def test_add_product_to_cart(self):
        self.driver.find_element("id", "user-name").send_keys("standard_user")
        self.driver.find_element("id", "password").send_keys("secret_sauce")
        self.driver.find_element("id", "login-button").click()
        self.driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element("class name", "shopping_cart_link").click()
        cart_items = self.driver.find_elements("class name", "cart_item")
        self.assertEqual(len(cart_items), 1)
