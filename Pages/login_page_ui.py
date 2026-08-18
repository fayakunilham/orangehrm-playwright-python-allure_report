from playwright.sync_api import Page, expect
import time

class LoginUIPage:

    def __init__(self, page: Page):
        self.page = page


    def verify_login_ui(self):
        self.page.goto(
                "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
                wait_until="domcontentloaded"
            )

        time.sleep(10)

        expect(
            self.page.get_by_role("heading", name="Login")
            ).to_be_visible()

        expect(
            self.page.locator("input[name='username']")
            ).to_be_visible()

        expect(
            self.page.locator("input[name='password']")
            ).to_be_visible()

        expect(
            self.page.get_by_role("button", name="Login")
            ).to_be_visible()

        expect(
            self.page.get_by_text("Forgot your password?")
            ).to_be_visible()