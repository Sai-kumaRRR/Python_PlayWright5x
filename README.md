# Learn Playwright

# How to create report Allure Reports
pip install pytest-playwright

# Allure
npm install allure-commandline
pip install allure-pytest
allure serve allure-reports
pip install pytest-html

pytest code/test_vwologin.py --html=reports.html