import pytest

from conftest import get_driver

from test.book_shop.pages.categories_page import CategoriesPage


class TestProductCategories:
    @pytest.mark.parametrize("category_name,num_products", [
        ("Signed", 1),
        ("Bestsellers", 2),
        ("Bookseller-picks", 3),
        ("Childrens", 5),
        ("Poetry", 3)
    ])
    def test_products_categories_access_functionality(self, get_driver, category_name, num_products):
        driver = get_driver
        categories_page = CategoriesPage(driver)
        categories_page.load_website()

        categories_page.click_on_a_category(category_name)
        assert categories_page.verify_category_is_loaded(category_name), "Category not loaded"
        assert categories_page.verify_categories_has_at_least_n_number_of_products(num_products), "n Products not found"
        categories_page.click_on_the_first_product()
        assert categories_page.verify_we_are_on_details_page_of_the_product(), "product details page is not loaded"
