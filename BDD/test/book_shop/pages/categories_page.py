import time

from selenium.webdriver.common.by import By

from .base import Base


class CategoriesPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_the_book_section(self):
        time.sleep(3)
        self.wait_and_get_element(By.CSS_SELECTOR, 'a[href="/booklists"]').click()

    def click_on_a_category(self, category_name):
        time.sleep(3)
        self.wait_and_get_element(By.CSS_SELECTOR, 'a[href="/booklists"]').click()
        time.sleep(3)
        self.wait_and_get_element(
            By.CSS_SELECTOR, f'a[href="?page=1&sort_by=&direction=DESC&filters[tag]={category_name}"]'
        ).click()

    def verify_category_is_loaded(self, category_name):
        time.sleep(3)
        return category_name in self.driver.current_url

    def verify_categories_has_at_least_n_number_of_products(self, number):
        time.sleep(3)
        products = self.wait_and_get_elements(By.CSS_SELECTOR, '.book-preview')
        return len(products) >= int(number)

    def click_on_the_first_product(self):
        time.sleep(3)
        target_element = self.wait_and_get_element(By.CSS_SELECTOR, '.book-preview')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
        target_element.click()

    def verify_we_are_on_details_page_of_the_product(self):
        time.sleep(3)
        return "stock" in self.driver.current_url
