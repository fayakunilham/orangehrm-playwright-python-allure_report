import re

from playwright.sync_api import Page, expect

from Pages.login_page_ui import LoginUIPage
from Utils.screenshot import Screenshot


class LoginPage:

    LOGIN_URL = (
        "https://opensource-demo.orangehrmlive.com/"
        "web/index.php/auth/login"
    )

    def __init__(self, page: Page, logger=None):

        self.page = page
        self.logger = logger

        # =====================================================
        # VERIFY LOGIN UI
        # =====================================================

        login_ui = LoginUIPage(page)
        login_ui.verify_login_ui()

        # =====================================================
        # LOCATORS
        # =====================================================

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

    # =========================================================
    # LOG HELPER
    # =========================================================

    def log(self, message):

        if self.logger:
            self.logger.info(message)

    # =========================================================
    # OPEN LOGIN
    # =========================================================

    def open(self):

        self.log(
            "LOGIN PAGE - Opening login page"
        )

        self.page.goto(
            self.LOGIN_URL,
            wait_until="domcontentloaded"
        )

        self.log(
            "LOGIN PAGE - Login page opened successfully"
        )

    # =========================================================
    # NEGATIVE LOGIN
    # =========================================================

    def negative_login(self, username, password):

        self.open()

        # -----------------------------------------------------
        # WAIT LOGIN FORM
        # -----------------------------------------------------

        self.log(
            "NEGATIVE LOGIN - Waiting for login form"
        )

        Screenshot.take(
            self.page,
            "Login Page Negative",
            wait_for=[
                self.username_input,
                self.password_input
            ],
            timeout=15000
        )

        # -----------------------------------------------------
        # INPUT CREDENTIALS
        # -----------------------------------------------------

        self.log(
            "NEGATIVE LOGIN - Filling username"
        )

        self.username_input.fill(username)

        self.log(
            "NEGATIVE LOGIN - Filling incorrect password"
        )

        self.password_input.fill(password)

        Screenshot.take(
            self.page,
            "The input was completed with an incorrect password"
        )

        # -----------------------------------------------------
        # CLICK LOGIN
        # -----------------------------------------------------

        self.log(
            "NEGATIVE LOGIN - Clicking Login button"
        )

        self.login_button.click()

        # -----------------------------------------------------
        # VERIFY ERROR MESSAGE
        # -----------------------------------------------------

        self.log(
            "NEGATIVE LOGIN - "
            "Verifying Invalid credentials message"
        )

        expect(
            self.invalid_credentials
        ).to_be_visible(
            timeout=10000
        )

        self.log(
            "NEGATIVE LOGIN - "
            "Invalid credentials message displayed"
        )

        Screenshot.take(
            self.page,
            "Login Failed"
        )

    # =========================================================
    # POSITIVE LOGIN
    # =========================================================

    def positive_login(self, username, password):

        self.open()

        # -----------------------------------------------------
        # WAIT LOGIN FORM
        # -----------------------------------------------------

        self.log(
            "POSITIVE LOGIN - Waiting for login form"
        )

        Screenshot.take(
            self.page,
            "Login Page Positive",
            wait_for=[
                self.username_input,
                self.password_input
            ],
            timeout=15000
        )

        # -----------------------------------------------------
        # INPUT CREDENTIALS
        # -----------------------------------------------------

        self.log(
            "POSITIVE LOGIN - Filling username"
        )

        self.username_input.fill(username)

        self.log(
            "POSITIVE LOGIN - Filling password"
        )

        self.password_input.fill(password)

        Screenshot.take(
            self.page,
            "The input was completed"
        )

        # -----------------------------------------------------
        # CLICK LOGIN
        # -----------------------------------------------------

        self.log(
            "POSITIVE LOGIN - Clicking Login button"
        )

        self.login_button.click()

        # -----------------------------------------------------
        # WAIT DASHBOARD URL
        # -----------------------------------------------------

        self.log(
            "POSITIVE LOGIN - Waiting for dashboard"
        )

        self.page.wait_for_url(
            "**/dashboard/**",
            timeout=10000
        )

        # -----------------------------------------------------
        # VERIFY DASHBOARD URL
        # -----------------------------------------------------

        self.log(
            "POSITIVE LOGIN - Verifying dashboard URL"
        )

        expect(
            self.page
        ).to_have_url(
            re.compile(r".*/dashboard/index")
        )

        # -----------------------------------------------------
        # VERIFY DASHBOARD HEADING
        # -----------------------------------------------------

        self.log(
            "POSITIVE LOGIN - Verifying Dashboard heading"
        )

        expect(
            self.dashboard_heading
        ).to_be_visible(
            timeout=10000
        )

        self.log(
            "POSITIVE LOGIN - Login successful"
        )

        Screenshot.take(
            self.page,
            "Login Success"
        )