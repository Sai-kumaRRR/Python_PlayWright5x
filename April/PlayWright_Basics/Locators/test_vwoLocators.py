import pytest
import allure


from playwright.sync_api import expect, sync_playwright


# Page - class -> help you interact with html
# expect - validate the message expected result == actual result
# validation -> pytest - assert also available


def test_login():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()

    # Load the page
    page.goto("https://app.vwo.com")
    # make page loaded
    page.wait_for_load_state("networkidle")

    # find the email and password
    # email id
    page.locator("#login-username").fill("admin")

    # password
    page.locator("#login-password").fill("password123")

    # click on the submit
    page.locator("#js-login-btn").click()

    # Verify the message

    error_message = page.locator("#js-notification-box-msg")

    expect(error_message).to_have_text("Your email, password, IP address or location did not match ")

    # dispose context once it is no longer needed
    context.close()
