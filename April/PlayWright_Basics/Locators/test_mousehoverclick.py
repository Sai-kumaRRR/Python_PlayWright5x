import time
import page
import pytest
from playwright.sync_api import sync_playwright

def test_keyboard_click():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/")
    page.locator("//a[normalize-space()='Broken Images']").click(modifiers=["Shift"])
    time.sleep(5)