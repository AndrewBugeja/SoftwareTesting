import pytest
from selenium import webdriver


@pytest.fixture
def get_driver():
    driver = webdriver.Chrome()
    yield driver
