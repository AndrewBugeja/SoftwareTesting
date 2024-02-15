import time

from selenium.webdriver.common.by import By

from .base import Base


class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_account_login(self):
        time.sleep(3)
        self.wait_and_get_element(By.CSS_SELECTOR, 'a[href="/account"]').click()

    def enter_email(self, email):
        time.sleep(3)
        self.wait_and_get_element(By.CSS_SELECTOR, '#form_email').send_keys(email)

    def enter_password(self, password):
        time.sleep(3)
        self.wait_and_get_element(By.CSS_SELECTOR, '#form_password').send_keys(password)

    def click_on_login_button(self):
        time.sleep(3)
        self.wait_and_get_element(By.CSS_SELECTOR, '#form_submit').click()

    def verify_my_profile_page_is_loaded(self):
        time.sleep(3)
        account_link = self.wait_and_get_element(By.CLASS_NAME, "account-link")
        time.sleep(3)
        return account_link.text
