import time
from asyncio import timeout

from playwright.sync_api import Page, expect

from Utils.screenshot import Screenshot


class AdminPage:

    def __init__(self, page: Page):
        self.page = page

        # Generate username unik setiap test dijalankan
        timestamp = int(time.time())

        self.username = f"Jalal{timestamp}1"
        self.password = "Admin123"

    # =========================================================
    # OPEN ADMIN
    # =========================================================

    def open_admin(self):

        self.page.get_by_text(
            "Admin",
            exact=True
        ).click()

        expect(
            self.page.get_by_role(
                "heading",
                name="Admin"
            )
        ).to_be_visible(
            timeout=10000
        )

        Screenshot.take(
            self.page,
            "19. Admin Page"
        )

    # =========================================================
    # SEARCH USER
    # =========================================================

    def search_user(self, username):
        username_field = self.page.locator(
            "input.oxd-input"
        ).nth(1)

        expect(
            username_field
        ).to_be_visible(
            timeout=10000
        )

        username_field.fill(username)

        self.page.wait_for_timeout(10000)

        self.page.wait_for_load_state(
            "domcontentloaded"
        )

        Screenshot.take(
            self.page,
            "22. Searching User Admin"
        )

        self.page.get_by_role(
            "button",
            name="Search"
        ).click()

        self.page.wait_for_load_state(
            "domcontentloaded"
        )

        Screenshot.take(
            self.page,
            "23. Search User Result"
        )
    # =========================================================
    # VERIFY USER
    # =========================================================

    def verify_user(self, username):

        expect(
            self.page.get_by_text(
                username,
                exact=True
            )
        ).to_be_visible(
            timeout=10000
        )

    # =========================================================
    # RESET SEARCH
    # =========================================================

    def reset_search(self):

        self.page.get_by_role(
            "button",
            name="Reset"
        ).click()

        self.page.wait_for_timeout(10000)

    # =========================================================
    # CLICK ADD
    # =========================================================

    def click_add(self):

        self.page.get_by_role(
            "button",
            name="Add"
        ).click()

        expect(
            self.page.get_by_role(
                "heading",
                name="Add User"
            )
        ).to_be_visible(
            timeout=10000
        )

        Screenshot.take(
            self.page,
            "20. Halaman Create user Admin"
        )

    # =========================================================
    # CREATE USER
    # =========================================================

    def create_user(self, employee_name):
        print("Employee Name :", employee_name)
        # =========================================
        # USER ROLE
        # =========================================

        user_role = self.page.locator(
            ".oxd-select-text"
        ).nth(0)

        user_role.click()

        self.page.get_by_text(
            "ESS",
            exact=True
        ).click()

        # =========================================
        # EMPLOYEE NAME
        # =========================================

        employee_field = self.page.get_by_placeholder(
            "Type for hints..."
        )

        employee_field.fill(
            employee_name
        )

        suggestion = self.page.locator(
            ".oxd-autocomplete-option"
        ).filter(
            has_text=employee_name
        ).first

        expect(
            suggestion
        ).to_be_visible(
            timeout=10000
        )

        suggestion.click()

        # =========================================
        # STATUS
        # =========================================

        status = self.page.locator(
            ".oxd-select-text"
        ).nth(1)

        status.click()

        self.page.get_by_text(
            "Enabled",
            exact=True
        ).click()

        # =========================================
        # USERNAME
        # =========================================

        print("===== DEBUG INPUT =====")

        print(
            "Jumlah input:",
            self.page.locator("input").count()
        )

        for i in range(self.page.locator("input").count()):
            locator = self.page.locator("input").nth(i)

            print(
                i,
                "type =", locator.get_attribute("type"),
                "name =", locator.get_attribute("name"),
                "placeholder =", locator.get_attribute("placeholder"),
                "value =", locator.input_value()
            )

        print("======================")

        username_field = self.page.locator(
            "input"
        ).nth(2)

        expect(
            username_field
        ).to_be_visible(
            timeout=10000
        )

        username_field.fill(
            self.username
        )

        expect(
            username_field
        ).to_have_value(
            self.username
        )

        print(
            "Username yang diinput:",
            username_field.input_value()
        )

        # =========================================
        # PASSWORD
        # =========================================

        password_fields = self.page.locator(
            "input[type='password']"
        )

        expect(
            password_fields.nth(0)
        ).to_be_visible(
            timeout=10000
        )

        password_fields.nth(0).fill(
            self.password
        )

        password_fields.nth(1).fill(
            self.password
        )

        # -----------------------------------------------------
        # SCREENSHOT BEFORE SAVE
        # -----------------------------------------------------

        Screenshot.take(
            self.page,
            "21. Before Save User Admin"
        )

        # -----------------------------------------------------
        # SAVE
        # -----------------------------------------------------

        self.page.get_by_role(
            "button",
            name="Save"
        ).click()

        self.page.wait_for_timeout(10000)

        Screenshot.take(
            self.page,
            "21. After Save User Admin"
        )

    # =========================================================
    # SEARCH CREATED USER
    # =========================================================

    def search_created_user(self):

        self.search_user(
            self.username
        )

        self.verify_user(
            self.username
        )

        Screenshot.take(
            self.page,
            "22. User Admin Found"
        )

    # =========================================================
    # EDIT USER
    # =========================================================

    def edit_user(self):
        row = self.page.locator(
            ".oxd-table-card"
        ).filter(
            has_text=self.username
        )

        expect(
            row
        ).to_be_visible(
            timeout=10000
        )

        # Klik icon pencil / Edit
        row.locator(
            "button:has(.bi-pencil-fill)"
        ).click()

        # Pastikan masuk halaman Edit User
        expect(
            self.page.get_by_role(
                "heading",
                name="Edit User"
            )
        ).to_be_visible(
            timeout=10000
        )

        Screenshot.take(
            self.page,
            "23. Before Edit User Admin"
        )

    # =========================================================
    # UPDATE USER
    # =========================================================

    def update_user(self):

        # -----------------------------------------------------
        # CHANGE STATUS
        # -----------------------------------------------------

        status = self.page.locator(
            ".oxd-select-text"
        ).nth(1)

        status.click()

        self.page.get_by_text(
            "Disabled",
            exact=True
        ).click()

        Screenshot.take(
            self.page,
            "24. After Edit User Admin"
        )

        # -----------------------------------------------------
        # SAVE
        # -----------------------------------------------------

        self.page.get_by_role(
            "button",
            name="Save"
        ).click()

        # -----------------------------------------------------
        # VERIFY SUCCESS
        # -----------------------------------------------------

        expect(
            self.page.get_by_text(
                "Successfully Updated"
            )
        ).to_be_visible(
            timeout=10000
        )

        Screenshot.take(
            self.page,
            "25. Succesfully Updated User Admin"
        )

    # =========================================================
    # DELETE USER
    # =========================================================

    def delete_user(self):
        self.page.go_back()

        # Cari user yang dibuat
        self.search_created_user()

        row = self.page.locator(
            ".oxd-table-card"
        ).filter(
            has_text=self.username
        )

        expect(
            row
        ).to_be_visible(
            timeout=10000
        )

        # -----------------------------------------------------
        # CLICK DELETE ICON
        # -----------------------------------------------------

        delete_button = row.locator(
            "button:has(.bi-trash)"
        )

        expect(
            delete_button
        ).to_be_visible(
            timeout=10000
        )

        delete_button.click()

        # -----------------------------------------------------
        # VERIFY DELETE CONFIRMATION
        # -----------------------------------------------------

        expect(
            self.page.get_by_text(
                "The selected record will be permanently deleted. Are you sure you want to continue?"
            )
        ).to_be_visible(
            timeout=10000
        )

        # -----------------------------------------------------
        # CONFIRM DELETE
        # -----------------------------------------------------

        self.page.get_by_role(
            "button",
            name="Yes, Delete"
        ).click()

        # -----------------------------------------------------
        # VERIFY SUCCESS
        # -----------------------------------------------------

        expect(
            self.page.get_by_text(
                "Successfully Deleted"
            )
        ).to_be_visible(
            timeout=10000
        )

        Screenshot.take(
            self.page,
            "Admin - User Deleted"
        )