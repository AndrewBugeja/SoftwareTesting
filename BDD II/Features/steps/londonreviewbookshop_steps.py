import time
from behave import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_and_get_element(context, strategy, locator, timeout=10):
    return WebDriverWait(context.driver, timeout=timeout).until(
        EC.presence_of_element_located((strategy, locator))
    )


def wait_and_get_elements(context, strategy, locator, timeout=20):
    try:
        elements = WebDriverWait(context.driver, timeout=timeout).until(
            EC.presence_of_all_elements_located((strategy, locator))
            )
    except TimeoutException:
        return []
    return elements


@given("I am a user of the website")
def step_given_user_of_website(context):
    pass


@when("I visit the news website")
def step_when_visit_news_website(context):
    context.driver.get("https://www.londonreviewbookshop.co.uk/")


@when('I click on the {category_name} category')
def step_click_on_category(context, category_name):
    time.sleep(3)
    wait_and_get_element(context, By.CSS_SELECTOR, 'a[href="/booklists"]').click()
    time.sleep(3)
    wait_and_get_element(context, By.CSS_SELECTOR,
                         f'a[href="?page=1&sort_by=&direction=DESC&filters[tag]={category_name}"]').click()


@then('I should be taken to {category_name} category')
def step_should_be_taken_to_category(context, category_name):
    time.sleep(3)
    assert category_name in context.driver.current_url, "Category not loaded"


@then('the category should show at least {num_products} products')
def step_category_should_show_products(context, num_products):
    time.sleep(3)
    products = wait_and_get_elements(context, By.CSS_SELECTOR, '.book-preview')
    assert len(products) >= int(num_products), "Products not found"


@when("I click on the first product in the results")
def step_click_on_first_product(context):
    time.sleep(3)
    target_element = wait_and_get_element(context, By.CSS_SELECTOR, '.book-preview')
    context.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
    target_element.click()


@then("I should be taken to the details page for that product")
def step_taken_to_details_page(context):
    time.sleep(3)
    assert "stock" in context.driver.current_url


"""
Search functionality
"""


@when('I search for a product using the term book')
def step_search_for_product(context):
    time.sleep(3)
    search_bar = wait_and_get_element(context, By.CSS_SELECTOR, '#search')
    search_bar.send_keys("book")
    time.sleep(3)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(3)
    wait_and_get_element(context, By.CSS_SELECTOR, '.lrb-arrowlink.mainLink').click()


@then('I should see the search results')
def step_should_see_search_results(context):
    time.sleep(3)
    assert "page=1" in context.driver.current_url, "No results found for the given search"


@then('there should be at least 5 products in the search results')
def step_check_min_products_in_results(context):
    time.sleep(3)
    products = wait_and_get_elements(context, By.CSS_SELECTOR, '.book-preview')
    assert len(products) >= 5, "less than 5 products found"


"""
Login functionality
"""


@when("I visit the login page")
def step_taken_to_go_to_login_page(context):
    time.sleep(3)
    wait_and_get_element(context,By.CSS_SELECTOR, 'a[href="/account"]').click()


@when("I enter the user email")
def step_taken_to_enter_user_email(context):
    time.sleep(3)
    wait_and_get_element(context, By.CSS_SELECTOR, '#form_email').send_keys("aeiou123@gmail.com")


@when("I enter the user password")
def step_taken_to_enter_user_password(context):
    time.sleep(3)
    wait_and_get_element(context, By.CSS_SELECTOR, '#form_password').send_keys("Abc123!@#")


@then("User should be logged in")
def step_taken_to_submit_login_details(context):
    time.sleep(3)
    wait_and_get_element(context, By.CSS_SELECTOR, '#form_submit').click()


"""
Add to cart and then remove 
"""


@when('I go to the books section')
def step_click_on_category(context):
    time.sleep(3)
    wait_and_get_element(context, By.CSS_SELECTOR, 'a[href="/booklists"]').click()


@when("I click on the add to cart button")
def step_taken_add_product_to_cart(context):
    time.sleep(3)
    wait_and_get_element(context, By.CSS_SELECTOR, '.btn.btn-primary.add-to-basket').click()
    time.sleep(2)
    product_added = wait_and_get_element(context, By.CSS_SELECTOR, 'button.btn.btn-primary.add-to-basket').text
    assert "added" in product_added.lower() or "go to basket" in product_added.lower(), \
        "Product could not be added to the cart"


@then("I go to the cart")
def step_taken_to_click_on_the_cart(context):
    time.sleep(3)
    wait_and_get_element(context, By.CSS_SELECTOR, '.basket-badge').click()


@then("I should be taken to the cart page")
def step_taken_to_details_page(context):
    time.sleep(3)
    assert "basket" in context.driver.current_url, "cart page is not loaded"


@then("I remove product from the cart")
def step_taken_to_remove_product_from_the_cart(context):
    time.sleep(2)
    product_before_removal = wait_and_get_element(context, By.CSS_SELECTOR, 'a.book-link')
    product_before_removal = product_before_removal.find_element(By.CSS_SELECTOR, '.book-title .ezstring-field').text
    wait_and_get_element(context, By.CSS_SELECTOR, '.btn.btn-secondary.closebtn.remove-item').click()
    time.sleep(5)
    element_after_removal = wait_and_get_elements(context, By.CSS_SELECTOR, 'a.book-link')
    if element_after_removal:
        product_names_after_removal = [element.find_element(By.CSS_SELECTOR, '.book-title .ezstring-field').text
                                       for element in element_after_removal]
        assert product_before_removal not in product_names_after_removal, \
            f'Book "{product_before_removal}" is still present after removal'
    else:
        assert True
