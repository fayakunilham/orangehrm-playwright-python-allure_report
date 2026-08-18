import random
import time
from pathlib import Path
from playwright.sync_api import Page, expect
from Utils.screenshot import Screenshot


class EmployeePage:

    def __init__(self, page: Page):
        self.page = page

        timestamp = int(time.time())

        self.first_name = f"Jalal{timestamp}"
        self.middle_name = "Lil"
        self.last_name = "Udin"
        self.new_last_name = "Jaenal"

        self.employee_id = str(random.randint(100000, 999999))

        self.username = f"Jalal{timestamp}"
        self.password = "Admin123!"

    # ====================================================
    # OPEN MENU
    # ====================================================

    def open_pim(self):
        self.page.get_by_role("link", name="PIM").click()

        self.page.wait_for_load_state("domcontentloaded")

        self.page.wait_for_timeout(10000)

        # Take Screenshot Pim Page
        Screenshot.take(self.page, "6. PIM Page")

    # ====================================================
    # CLICK ADD
    # ====================================================

    def click_add(self):

        self.open_pim()

        self.page.get_by_role("button", name="Add").click()

        self.page.wait_for_timeout(10000)

        expect(
            self.page.get_by_role("heading", name="Add Employee")
        ).to_be_visible(timeout=10000)

        # Take Screenshot Add User
        Screenshot.take(self.page, "7. Add User Page (PIM)")

        # ====================================================
    # CREATE EMPLOYEE
    # ====================================================

    def create_employee(self):

        # -----------------------
        # Upload Photo
        # -----------------------

        photo = Path("assets/profile.jpg")

        self.page.locator("input[type='file']").set_input_files(photo)

        self.page.wait_for_timeout(10000)

        Screenshot.take(self.page, "8. Upload Profile")

        # -----------------------
        # Employee Information
        # -----------------------

        self.page.locator("input[name='firstName']").fill(
            self.first_name
        )

        self.page.locator("input[name='middleName']").fill(
            self.middle_name
        )

        self.page.locator("input[name='lastName']").fill(
            self.last_name
        )

        # Employee Full Name
        employee_id = self.page.locator(
            "input.oxd-input"
        ).nth(4)

        employee_id.clear()

        employee_id.fill(self.employee_id)

        self.page.wait_for_timeout(10000)

        #Screenshoot Employee Full Name
        Screenshot.take(self.page, "9. Employee Full Name")

        # -----------------------
        # Create Login Details
        # -----------------------

        self.page.locator(".oxd-switch-input").click()

        # Username
        self.page.locator(
            "input.oxd-input"
        ).nth(5).fill(
            self.username
        )

        # Status
        self.page.get_by_role(
            "radio",
            name="Enabled"
        ).check()

        # Password
        self.page.locator(
            "input[type='password']"
        ).nth(0).fill(
            self.password
        )

        # Confirm Password
        self.page.locator(
            "input[type='password']"
        ).nth(1).fill(
            self.password
        )

        self.page.wait_for_timeout(10000)

        #Screenshot Create Login Details
        Screenshot.take(self.page, "10. Create Login Details")

        # -----------------------
        # Save
        # -----------------------

        self.page.get_by_role(
            "button",
            name="Save"
        ).click()

        # Tunggu redirect
        self.page.wait_for_url(
            "**/viewPersonalDetails/**",
            timeout=10000
        )

        # Screenshot Create user Success
        Screenshot.take(self.page, "11. Create user Success")

        # Validasi berhasil
    def waiting_personal_detail(self):
        expect(
            self.page.get_by_role(
                "heading",
                name="Personal Details"
            )
        ).to_be_visible(timeout=10000)

        # Screenshot Validasi berhasil
        Screenshot.take(self.page, "12. Validasi berhasil")

        # =================================
        # RETURN EMPLOYEE NAME
        # =================================

        employee_name = f"{self.first_name} {self.middle_name} {self.last_name}"

        print("Employee Name dari PIM:", employee_name)

        return employee_name

    # =========================
    # SEARCH
    # =========================

    def search_employee(self):

        self.open_pim()

        employee = self.page.locator(
            "input[placeholder='Type for hints...']"
        ).first

        employee.fill(self.first_name)

        self.page.wait_for_timeout(10000)

        self.page.wait_for_load_state("domcontentloaded")

        # Take Screenshot Searching User
        Screenshot.take(self.page, "13. Searching user")

        if self.page.locator(".oxd-autocomplete-option").count() > 0:
            self.page.locator(".oxd-autocomplete-option").first.click()

        self.page.get_by_role("button", name="Search").click()

        self.page.wait_for_load_state("domcontentloaded")

        # Take Screenshot Open page Update data User
        Screenshot.take(self.page, "14. Open page Update data User")

    # =========================
    # UPDATE
    # =========================

    def click_update(self):

        row = self.page.locator(".oxd-table-row").filter(
            has_text=self.first_name
        )

        row.locator("button").first.click()

    def update_employee(self):

        lastname = self.page.locator("input[name='lastName']")

        lastname.clear()

        lastname.fill(self.new_last_name)

        self.page.wait_for_timeout(10000)

        self.page.wait_for_load_state("domcontentloaded")

        # Screenshot Complete input data for Update User
        Screenshot.take(self.page, "15. Complete input data for Update User")

        self.page.get_by_role("button", name="Save").nth(0).click()

        self.page.wait_for_timeout(10000)

        # Screenshot Complete input data for Update User
        Screenshot.take(self.page, "16. Success Update User")

    # =========================
    # DELETE
    # =========================

    def delete_employee(self):

        self.open_pim()

        self.search_employee()

        row = self.page.locator(".oxd-table-row").filter(
            has_text=self.first_name
        )

        row.locator("button").nth(1).click()

        self.page.wait_for_load_state("domcontentloaded")

        # Screenshot Pop Up Confirmation Delete data User
        Screenshot.take(self.page, "17. Pop Up Confirmation Delete data User")

        self.page.get_by_role(
            "button",
            name="Yes, Delete"
        ).click()

        self.page.wait_for_load_state("domcontentloaded")

        # Take Screenshot Success Delete User
        Screenshot.take(self.page, "18. Success Delete User")