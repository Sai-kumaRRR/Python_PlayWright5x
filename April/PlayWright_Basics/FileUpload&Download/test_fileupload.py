import os
import time
import pytest
import page

from playwright.sync_api import sync_playwright


def test_file_upload():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/upload")

    cwd = os.getcwd()
    print(cwd)

    with page.expect_file_chooser() as fc:
        page.locator("#file-upload").click()
    file_c = fc.value

    file_c.set_files(cwd + "/Playwright_File_Upload_Guide.pdf")
    page.locator("//input[@id='file-submit']").click()
    page.wait_for_load_state()

    time.sleep(5)
