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

@pytest.mark.negative()
def test_vwo_login_negative(setUp):
    page = setUp
    # Load the Page
    page.goto("https://selectorshub.com/xpath-practice-page/")
    # Make page loaded
    page.wait_for_load_state("networkidle")

    div = page.locator("xpath=//div[@class='jackPart']")
    div.scroll_into_view_if_needed()

    # Directly interact with shadow dom
    link = page.locator("div.jackPart #app2 #pizza")
    print(link.input_value())
    link.fill("Farmhouse")

    time.sleep(20)