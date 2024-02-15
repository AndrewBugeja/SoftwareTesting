from conftest import get_driver

from test.book_shop.pages.login_page import LoginPage


class TestLogin:

    def test_login_functionality(self, get_driver):
        driver = get_driver
        login_page = LoginPage(driver)
        login_page.load_website()
        login_page.click_on_account_login()
        login_page.enter_email("aeiou123@gmail.com")
        login_page.enter_password("Abc123!@#")
        login_page.click_on_login_button()
        assert login_page.verify_my_profile_page_is_loaded() == "My Account", "Login not successful"
