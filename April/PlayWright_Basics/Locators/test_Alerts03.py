import pytest
import allure
import page
import time

from playwright.sync_api import sync_playwright

@pytest.fixture()
def setUp():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page
    yield page
    page.close()
    context.close()

@pytest.mark.negative
def test_JS_alerts(setUp):
    page = setUp
    # Load the Page
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    # Make page loaded
    page.wait_for_load_state("networkidle")

    page.on('dialog',lambda dialog: dialog.accept("SAI"))
   #page.on('dialog', lambda dialog: dialog.dismiss())
    page.locator("//button[@onclick='jsPrompt()']").click()
    result = page.locator("//p[@id='result']").text_content()
    # assert result == "You clicked: Cancel"
    assert result == "You entered: SAI"


    time.sleep(5)