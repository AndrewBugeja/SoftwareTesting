from conftest import get_driver

from test.book_shop.pages.cart import Cart
from test.book_shop.pages.categories_page import CategoriesPage
from test.book_shop.pages.login_page import LoginPage


class TestCart:
    def test_cart_functionality(self, get_driver):
        driver = get_driver
        login = LoginPage(driver)
        categories_page = CategoriesPage(driver)
        cart = Cart(driver)

        login.load_website()
        login.click_on_account_login()
        login.enter_email("aeiou123@gmail.com")
        login.enter_password("Abc123!@#")
        login.click_on_login_button()

        categories_page.go_to_the_book_section()
        categories_page.click_on_the_first_product()
        categories_page.verify_we_are_on_details_page_of_the_product()

        cart.click_on_add_to_cart_button()
        assert cart.verify_product_is_added_to_the_cart(), "Product could not be added to the cart"
        cart.click_on_the_cart()
        assert cart.verify_cart_is_loaded(), "cart page is not loaded"
        assert cart.remove_product_from_the_cart()

