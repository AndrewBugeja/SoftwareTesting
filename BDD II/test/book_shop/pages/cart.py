import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import Base


class Cart(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_add_to_cart_button(self):
        time.sleep(3)
        self.wait_and_get_element(By.CSS_SELECTOR, '.btn.btn-primary.add-to-basket').click()

    def verify_product_is_added_to_the_cart(self):
        time.sleep(2)
        product_added = self.wait_and_get_element(By.CSS_SELECTOR, 'button.btn.btn-primary.add-to-basket').text
        return "added" in product_added.lower() or "go to basket" in product_added.lower()

    def click_on_the_cart(self):
        time.sleep(3)
        self.wait_and_get_element(By.CSS_SELECTOR, '.basket-badge').click()

    def verify_cart_is_loaded(self):
        time.sleep(3)
        return "basket" in self.driver.current_url

    def remove_product_from_the_cart(self):
        time.sleep(2)
        product_before_removal = self.wait_and_get_element(By.CSS_SELECTOR, 'a.book-link')
        product_before_removal = product_before_removal.find_element(By.CSS_SELECTOR,
                                                                     '.book-title .ezstring-field').text
        self.wait_and_get_element(By.CSS_SELECTOR, '.btn.btn-secondary.closebtn.remove-item').click()
        time.sleep(5)
        element_after_removal = self.wait_and_get_elements(By.CSS_SELECTOR, 'a.book-link')
        if element_after_removal:
            product_names_after_removal = [element.find_element(By.CSS_SELECTOR, '.book-title .ezstring-field').text
                                           for element in element_after_removal]
            return product_before_removal not in product_names_after_removal, \
                f'Book "{product_before_removal}" is still present after removal'
        else:
            return True
