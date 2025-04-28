import pytest
import allure
import page
import time

from playwright.sync_api import sync_playwright


# Page - class -> help you interact with html
# expect - validate the message expected result == actual result
# validation -> pytest - assert also available

@pytest.fixture()
def setUp():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page
    yield page
    page.close()
    context.close()


def test_vwo_login_negative(setUp):
    page = setUp
    # Load the Page
    page.goto("https://app.vwo.com/#/login")
    # Make page loaded
    page.wait_for_load_state("networkidle")
    page.locator("//input[@id='login-username']").fill("admin")
    page.locator("//input[@id='login-password']").fill("admin")
    page.locator("//button[@id='js-login-btn']").click()

    error_msg_selc = "//div[@id='js-notification-box-msg']"
    page.wait_for_selector(error_msg_selc)

    error_msg = page.locator(error_msg_selc)

    assert error_msg.text_content() == "Your email, password, IP address or location did not match"

    # dispose context once it is no longer needed


def test_vwo_login_positive(setUp):
    page = setUp
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Load the Page
    page.goto("https://app.vwo.com/#/login")
    # Make page loaded
    page.wait_for_load_state("networkidle")
    page.locator("//input[@id='login-username']").fill("admin")
    page.locator("//input[@id='login-password']").fill("admin")
    page.locator("//button[@id='js-login-btn']").click()

    error_msg_selc = "//div[@id='js-notification-box-msg']"
    page.wait_for_selector(error_msg_selc)

    error_msg = page.locator(error_msg_selc)

    assert error_msg.text_content() == "Your email, password, IP address or location did not match"
