from selenium import webdriver


def before_all(context):
    # Initialize your driver here (you might want to configure it based on your needs)
    context.driver = webdriver.Chrome()


def after_all(context):
    # Close the driver after all scenarios are executed
    context.driver.quit()
