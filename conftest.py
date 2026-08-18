import pytest
from playwright.sync_api import sync_playwright
from Pages.login_page import LoginPage

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.set_default_timeout(10_000)
        page.set_default_navigation_timeout(30_000)

        yield page
        browser.close()

@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.positive_login(
        "Admin",
        "admin123"
    )

    return page