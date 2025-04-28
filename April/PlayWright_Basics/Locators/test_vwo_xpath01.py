import time
import pytest
import allure
import page

from playwright.sync_api import sync_playwright


# Page - class -> help you interact with html
# expect - validate the message expected result == actual result
# validation -> pytest - assert also available


def test_vwo_login():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Load the Page
    page.goto("https://awesomeqa.com/pw/locators1.html")
    # Make page loaded
    page.wait_for_load_state("networkidle")
    page.locator("[data-qa='hocewoqisi']").fill("admin@admin.com")
    page.locator("a#btn-make-appointment")
    page.locator("//a[@id='btn-make-appointment']").fill("admin@admin.com")

    # write your code here

    time.sleep(10)

    # dispose context once it is no longer needed
    context.close()
