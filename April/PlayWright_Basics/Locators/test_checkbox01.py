import pytest
import allure
import page
import time

from playwright.sync_api import sync_playwright

@pytest.mark.test
def test_check_box():
    # Boilerplate  code to star the playwright
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
     # load the page
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    # make page loaded
    page.wait_for_load_state("networkidle")
    page.get_by_role("checkbox").first.click()
    page.get_by_role("checkbox").last.click()

    time.sleep(5)



