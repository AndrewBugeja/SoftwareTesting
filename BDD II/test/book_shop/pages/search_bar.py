import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import Base


class SearchBar(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def search_a_book(self, book):
        time.sleep(3)
        search_bar = self.wait_and_get_element(By.CSS_SELECTOR, '#search')
        search_bar.send_keys(book)
        time.sleep(3)
        search_bar.send_keys(Keys.RETURN)
        time.sleep(3)
        self.wait_and_get_element(By.CSS_SELECTOR, '.lrb-arrowlink.mainLink').click()

    def verify_search_results_shown(self):
        time.sleep(3)
        return "page=1" in self.driver.current_url
