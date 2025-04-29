import pytest
from playwright.sync_api import sync_playwright


def test_lab01():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amcharts.com/svg-maps/?map=india")

    # Handling a list of SVG elements
    states_list = page.locator("xpath=//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='path']")

    # Iterating over elements and performing an action
    print(states_list)
    assert pytest.xfail("Custom Fail")

    # page.pause()
    page.close()
    context.close()
    browser.close()