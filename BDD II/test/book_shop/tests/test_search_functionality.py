import pytest

from conftest import get_driver

from test.book_shop.pages.categories_page import CategoriesPage
from test.book_shop.pages.search_bar import SearchBar


class TestSearch:

    def test_search_functionality(self, get_driver):
        driver = get_driver
        categories_page = CategoriesPage(driver)
        search_bar = SearchBar(driver)
        categories_page.load_website()

        search_bar.search_a_book("book")
        assert search_bar.verify_search_results_shown()
        assert categories_page.verify_categories_has_at_least_n_number_of_products(5)
        categories_page.click_on_the_first_product()
        assert categories_page.verify_we_are_on_details_page_of_the_product()

