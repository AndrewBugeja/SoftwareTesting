import pytest
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver

    def load_website(self):
        self.driver.get("https://www.londonreviewbookshop.co.uk/")

    def wait_and_get_element(self, strategy, locator, timeout=30):
        return WebDriverWait(self.driver, timeout=timeout).until(
            EC.presence_of_element_located((strategy, locator))
        )

    def wait_and_get_elements(self, strategy, locator, timeout=20):
        try:
            elements = WebDriverWait(self.driver, timeout=timeout).until(
                EC.presence_of_all_elements_located((strategy, locator))
            )
        except TimeoutException:
            return []
        return elements

