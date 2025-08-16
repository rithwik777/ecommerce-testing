from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest
import time


@pytest.fixture
def setup():
    # ✅ Chrome setup (ChromeDriver 139 must be in your project folder)
    options = Options()
    service = Service("./chromedriver.exe")  # update path if needed

    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


# -----------------------------
# ✅ Positive Test Cases
# -----------------------------

def test_login_valid(setup):
    driver = setup
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    assert "inventory" in driver.current_url


def test_add_to_cart(setup):
    driver = setup
    # Login first
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Add product to cart
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    # Verify product is added
    product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert product_name != ""


def test_checkout_process(setup):
    driver = setup
    # Login first
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Add product & go to cart
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # Enter details
    driver.find_element(By.ID, "first-name").send_keys("Rithwik")
    driver.find_element(By.ID, "last-name").send_keys("M")
    driver.find_element(By.ID, "postal-code").send_keys("500001")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()

    # Verify checkout success
    confirmation = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "THANK YOU" in confirmation


# -----------------------------
# ❌ Negative Test Cases
# -----------------------------

def test_login_invalid(setup):
    driver = setup
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error_message


def test_checkout_missing_info(setup):
    driver = setup
    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Add product & go to checkout
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # Leave all fields empty
    driver.find_element(By.ID, "first-name").send_keys("")
    driver.find_element(By.ID, "last-name").send_keys("")
    driver.find_element(By.ID, "postal-code").send_keys("")
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    # Verify error
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Error" in error_message
