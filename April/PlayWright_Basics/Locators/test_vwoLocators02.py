import page
import pytest
import allure


from playwright.sync_api import expect, sync_playwright


# Page - class -> help you interact with html
# expect - validate the message expected result == actual result
# validation -> pytest - assert also available


def test_vwo_login():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Load the Page
    page.goto("https://app.vwo.com")
    # Make page loaded
    page.wait_for_load_state("networkidle")

    # Find the email and password
    # Email ID
    page.get_by_role("textbox", name="Email address").fill("admin")

    # Password
    page.get_by_role("textbox", name="Password").fill("admin")

    # Click on the submit
    page.locator("#js-login-btn").click()

    # Verify the message

    error_message = page.locator("#js-notification-box-msg")

    expect(error_message).to_have_text("Your email, password, IP address or location did not match ")

    # dispose context once it is no longer needed
    context.close()
