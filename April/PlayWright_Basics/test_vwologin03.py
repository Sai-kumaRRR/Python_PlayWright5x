import pytest
import allure

from playwright.sync_api import Page, expect, sync_playwright

# Page - class -> help you interact with html
#expect - validate the message expected result == actual result
# validation -> pytest - assert also available
#    one page -> 2 context

def test_login():

    #1.)  Browser and Page
    browser = sync_playwright().start().chromium.launch(headless=False)
  #create a new incognito browser context
    context = browser.new_context()

    page = browser.new_page()
    page2 = context.new_page()

    #2.) code interaction with Html page
    page.goto("https://app.vwo.com")
    page2.goto("https://bing.com")


    #3.) Validation
    expect(page).to_have_title(" Login - VWO.COM")

    #dispose context once it is no longer needed
    context.close()
