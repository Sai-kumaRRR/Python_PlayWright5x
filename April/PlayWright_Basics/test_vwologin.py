import pytest
import allure

from playwright.sync_api import Page, expect, sync_playwright

# Page - class -> help you interact with html
#expect - validate the message expected result == actual result
# validation -> pytest - assert also available

def test_login():

    # Browser and Page
    browser = sync_playwright().start().chromium.launch(headless=False)

    page = browser.new_page()
    # code interaction with Html page
    page.goto("https://app.vwo.com")
    # Validation
    expect(page).to_have_title(" Login - VWO.COM")
