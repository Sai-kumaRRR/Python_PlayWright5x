import time

import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.test
def test_check_box02():
    # Boilerplate  code to star the playwright
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # load the page
    page.goto("https://awesomeqa.com/practice.html")
    # make page loaded
    page.wait_for_load_state("networkidle")
    page.locator("//input[@id='profession-0']").click()

    time.sleep(5)
