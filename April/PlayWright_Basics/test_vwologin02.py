import pytest
import allure

from playwright.sync_api import Page, expect, sync_playwright

# Page - class -> help you interact with html
#expect - validate the message expected result == actual result
# validation -> pytest - assert also available
# breakpoint()

def test_login():

    #1.)  Browser and Page
    browser = sync_playwright().start().chromium.launch(headless=False)

    page = browser.new_page()
    #2.) code interaction with Html page
    page.goto("https://app.vwo.com")
    breakpoint()

    #3.) Validation
    expect(page).to_have_title(" Login - VWO.COM")
