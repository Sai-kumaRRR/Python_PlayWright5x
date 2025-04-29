import time
from playwright.sync_api import sync_playwright

def test_lab01():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.vwo.com/#/login",wait_until="networkidle")
    page.locator("#login-username").fill("saiprashant3143@gamil.com")
    page.locator("#login-password").fill("Sai@2025")
    page.click("#js-login-btn", timeout=5000)

    page.wait_for_selector("//span[@data-qa='lufexuloga']")
    heading = page.locator ("//span[@data-qa='lufexuloga']").text_content()
    assert heading == "Sai"
    time.sleep(5)
