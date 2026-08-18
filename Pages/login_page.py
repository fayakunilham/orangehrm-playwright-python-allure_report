import re
import time
from playwright.sync_api import Page, expect
from Pages.login_page_ui import LoginUIPage
from Utils.screenshot import Screenshot


class LoginPage:
    LOGIN_URL = (
        "https://opensource-demo.orangehrmlive.com/"
        "web/index.php/auth/login"
    )

    def __init__(self, page: Page):
        self.page = page

        login_ui = LoginUIPage(page)
        login_ui.verify_login_ui()

        self.username_input = page.locator(
            "input[name='username']"
        )
        self.password_input = page.locator(
            "input[name='password']"
        )
        self.login_button = page.get_by_role(
            "button",
            name="Login"
        )
        self.dashboard_heading = page.get_by_role(
            "heading",
            name="Dashboard"
        )
        self.invalid_credentials = page.get_by_text(
            "Invalid credentials"
        )

    # =========================
    # OPEN LOGIN
    # =========================

    def open(self):
        self.page.goto(
            self.LOGIN_URL,
            wait_until="domcontentloaded"
        )

    # =========================
    # NEGATIVE LOGIN
    # =========================

    def negative_login(self, username, password):
        self.open()

        Screenshot.take(
            self.page,
            "1. Login Page Negative"
        )

        self.page.locator("input[name='username']").fill(username)
        self.page.locator("input[name='password']").fill(password)

        Screenshot.take(
            self.page,
            "2. The input was completed with an incorrect password"
        )

        self.page.get_by_role("button", name="Login").click()

        expect(
            self.page.get_by_text("Invalid credentials")
        ).to_be_visible(timeout=10000)

        Screenshot.take(
            self.page,
            "3. Login Failed"
        )

    #Positive Login
    def positive_login(self, username, password):

        self.open()

        Screenshot.take(
            self.page,
            "4. Login Page Positive"
        )

        self.page.locator("input[name='username']").fill(username)
        self.page.locator("input[name='password']").fill(password)

        Screenshot.take(
            self.page,
            "4. The input was completed"
        )

        self.page.get_by_role("button", name="Login").click()

        self.page.wait_for_timeout(10000)

        self.page.wait_for_url(
            "**/dashboard/**",
            timeout=10000
        )

        expect(self.page).to_have_url(
            re.compile(r".*/dashboard/index")
        )

        expect(
            self.page.get_by_role("heading", name="Dashboard")
        ).to_be_visible()

        self.page.wait_for_timeout(10000)

        Screenshot.take(
            self.page,
            "5. Login Success"
        )