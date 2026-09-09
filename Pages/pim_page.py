import re
import random
import time
from pathlib import Path

from playwright.sync_api import Page, expect

from Utils.screenshot import Screenshot


class EmployeePage:

    def __init__(self, page: Page, logger=None):

        # ==========================================================
        # INITIALIZE PLAYWRIGHT PAGE
        # ==========================================================

        self.page = page

        # ==========================================================
        # INITIALIZE LOGGER
        # ==========================================================

        self.logger = logger

        # ==========================================================
        # GENERATE UNIQUE TEST DATA
        # ==========================================================

        timestamp = int(time.time())

        # Generate employee first name
        self.first_name = f"Jalal{timestamp}"

        # Generate employee middle name
        self.middle_name = "Lil"

        # Generate employee last name
        self.last_name = "Udin"

        # Generate new last name for update test
        self.new_last_name = "Jaenal"

        # Generate random employee ID
        self.employee_id = str(
            random.randint(100000, 999999)
        )

        # Generate unique username
        self.username = f"Jalal{timestamp}"

        # Password for test user
        self.password = "Admin123!"

    # ==========================================================
    # LOG HELPER
    # ==========================================================

    def log(self, message):

        # Write message to logger if logger is available
        if self.logger:
            self.logger.info(message)

    # ==========================================================
    # OPEN PIM MENU
    # ==========================================================

    def open_pim(self):

        self.log(
            "PIM - Opening PIM menu"
        )

        # Click PIM menu
        self.page.get_by_role(
            "link",
            name="PIM"
        ).click()

        self.log(
            "PIM - Waiting for Records Found"
        )

        # Wait until Records Found is visible
        records_found = self.page.get_by_text(
            re.compile(r"\(\d+\)\s+Records?\s+Found")
        )

        expect(
            records_found
        ).to_be_visible(
            timeout=15000
        )

        self.log(
            "PIM - Records Found is visible"
        )

        # Take screenshot of PIM page
        Screenshot.take(
            self.page,
            "PIM Page",
            wait_for=records_found,
            timeout=20000
        )

        self.log(
            "PIM - PIM page opened successfully"
        )

    # ==========================================================
    # CLICK ADD EMPLOYEE
    # ==========================================================

    def click_add(self):

        self.log(
            "CREATE - Opening Add Employee page"
        )

        # Open PIM menu
        self.open_pim()

        # Click Add button
        self.page.get_by_role(
            "button",
            name="Add"
        ).click()

        self.log(
            "CREATE - Add button clicked"
        )

        # Wait until Records Found is visible
        logindetails = self.page.get_by_text(
            re.compile("Create Login Details")
        )

        expect(
            logindetails
        ).to_be_visible(
            timeout=15000
        )

        # Locate Add Employee heading
        add_employee_heading = self.page.get_by_role(
            "heading",
            name="Add Employee",
            exact=True
        )

        # Wait until Add Employee page is visible
        expect(
            add_employee_heading
        ).to_be_visible(
            timeout=15000
        )

        self.log(
            "CREATE - Add Employee page opened successfully"
        )

        # Take screenshot of Add Employee page
        Screenshot.take(
            self.page,
            "Add User Page (PIM)",
            wait_for=[
                logindetails,
                add_employee_heading,
                self.page.get_by_role(
                    "button",
                    name="Save"
                )
            ],
            timeout=15000
        )

    # ==========================================================
    # CREATE EMPLOYEE
    # ==========================================================

    def create_employee(self):

        self.log(
            "CREATE - Starting employee creation"
        )

        # ======================================================
        # UPLOAD PROFILE PHOTO
        # ======================================================

        self.log(
            "CREATE - Uploading profile photo"
        )

        # Define profile photo path
        photo = Path(
            "assets/profile.jpg"
        )

        # Locate file upload input
        file_input = self.page.locator(
            "input[type='file']"
        )

        # Upload profile photo
        file_input.set_input_files(
            photo
        )

        self.log(
            "CREATE - Profile photo uploaded successfully"
        )

        # Take screenshot after upload
        Screenshot.take(
            self.page,
            "Upload Profile"
        )

        # ======================================================
        # EMPLOYEE INFORMATION
        # ======================================================

        self.log(
            "CREATE - Filling employee information"
        )

        # Fill first name
        self.page.locator(
            "input[name='firstName']"
        ).fill(
            self.first_name
        )

        # Fill middle name
        self.page.locator(
            "input[name='middleName']"
        ).fill(
            self.middle_name
        )

        # Fill last name
        self.page.locator(
            "input[name='lastName']"
        ).fill(
            self.last_name
        )

        # Locate Employee ID input
        employee_id = self.page.locator(
            "input.oxd-input"
        ).nth(4)

        # Clear existing Employee ID
        employee_id.clear()

        # Fill generated Employee ID
        employee_id.fill(
            self.employee_id
        )

        self.log(
            f"CREATE - Employee information filled: "
            f"{self.first_name} {self.middle_name} {self.last_name}"
        )

        # Take screenshot of employee information
        Screenshot.take(
            self.page,
            "Employee Full Name",
            wait_for=[
                self.page.locator(
                    "input[name='firstName']"
                ),
                self.page.locator(
                    "input[name='middleName']"
                ),
                self.page.locator(
                    "input[name='lastName']"
                )
            ],
            timeout=15000
        )

        # ======================================================
        # CREATE LOGIN DETAILS
        # ======================================================

        self.log(
            "CREATE - Enabling Create Login Details"
        )

        # Enable Create Login Details switch
        self.page.locator(
            ".oxd-switch-input"
        ).click()

        # Locate username input
        username_input = self.page.locator(
            "input.oxd-input"
        ).nth(5)

        # Wait until username input is visible
        expect(
            username_input
        ).to_be_visible(
            timeout=15000
        )

        # Fill username
        username_input.fill(
            self.username
        )

        self.log(
            f"CREATE - Username filled: {self.username}"
        )

        # Select Enabled status
        self.page.get_by_role(
            "radio",
            name="Enabled"
        ).check()

        # Locate password fields
        password_fields = self.page.locator(
            "input[type='password']"
        )

        # Fill password
        password_fields.nth(0).fill(
            self.password
        )

        # Fill confirm password
        password_fields.nth(1).fill(
            self.password
        )

        self.log(
            "CREATE - Login details completed"
        )

        # Take screenshot of login details
        Screenshot.take(
            self.page,
            "Create Login Details",
            wait_for=[
                username_input,
                password_fields.nth(0),
                password_fields.nth(1),
                self.page.get_by_role(
                    "button",
                    name="Save"
                )
            ],
            timeout=15000
        )

        # ======================================================
        # SAVE EMPLOYEE
        # ======================================================

        self.log(
            "CREATE - Clicking Save button"
        )

        # Click Save button
        self.page.get_by_role(
            "button",
            name="Save"
        ).click()

        # ======================================================
        # WAIT FOR PERSONAL DETAILS PAGE
        # ======================================================

        self.log(
            "CREATE - Waiting for Personal Details page"
        )

        personal_details = self.page.get_by_role(
            "heading",
            name="Personal Details",
            exact=True
        )

        # Wait until Personal Details is visible
        expect(
            personal_details
        ).to_be_visible(
            timeout=30000
        )

        self.page.wait_for_load_state(
            "domcontentloaded"
        )

        self.log(
            "CREATE - Personal Details page opened successfully"
        )

        # ======================================================
        # SCREENSHOT CREATE USER SUCCESS
        # ======================================================

        Screenshot.take(
            self.page,
            "Create User Success",
            wait_for=[
                personal_details,
                self.page.get_by_text(
                    "Employee Full Name",
                    exact=True
                ),
                self.page.get_by_role(
                    "heading",
                    name="Custom Fields",
                    exact=True
                ),
                self.page.get_by_role(
                    "heading",
                    name="Attachments",
                    exact=True
                )
            ],
            timeout=30000
        )

        self.log(
            f"CREATE - Employee created successfully: "
            f"{self.first_name} {self.middle_name} {self.last_name}"
        )

    # ==========================================================
    # VALIDATE PERSONAL DETAILS
    # ==========================================================

    def waiting_personal_detail(self):

        self.log(
            "VALIDATE - Checking Personal Details"
        )

        # Locate Personal Details heading
        personal_details = self.page.get_by_role(
            "heading",
            name="Personal Details",
            exact=True
        )

        # Validate Personal Details is visible
        expect(
            personal_details
        ).to_be_visible(
            timeout=15000
        )

        # Take screenshot of validation result
        Screenshot.take(
            self.page,
            "Validasi berhasil",
            wait_for=personal_details,
            timeout=15000
        )

        # ======================================================
        # CREATE EMPLOYEE FULL NAME
        # ======================================================

        employee_name = (
            f"{self.first_name} "
            f"{self.middle_name} "
            f"{self.last_name}"
        )

        # Write employee name to log
        self.log(
            f"VALIDATE - Employee Name dari PIM: "
            f"{employee_name}"
        )

        # Return employee name
        return employee_name

    # ==========================================================
    # SEARCH EMPLOYEE
    # ==========================================================

    def search_employee(self):

        self.log(
            f"READ - Searching employee: "
            f"{self.first_name}"
        )

        # Open PIM menu
        self.open_pim()

        # Locate employee search input
        employee = self.page.locator(
            "input[placeholder='Type for hints...']"
        ).first

        # Fill employee name
        employee.fill(
            self.first_name
        )

        self.log(
            f"READ - Employee search keyword entered: "
            f"{self.first_name}"
        )

        # Locate autocomplete option
        autocomplete = self.page.locator(
            ".oxd-autocomplete-option"
        )

        # Wait for autocomplete result
        autocomplete.first.wait_for(
            state="visible",
            timeout=15000
        )

        self.log(
            "READ - Autocomplete employee found"
        )

        # Take screenshot while searching
        Screenshot.take(
            self.page,
            "Searching User",
            wait_for=autocomplete.first,
            timeout=15000
        )

        # Click first autocomplete result
        autocomplete.first.click()

        self.log(
            "READ - Employee selected from autocomplete"
        )

        # Click Search button
        self.page.get_by_role(
            "button",
            name="Search"
        ).click()

        self.log(
            "READ - Search button clicked"
        )

        # Locate employee table row
        employee_row = self.page.locator(
            ".oxd-table-row"
        ).filter(
            has_text=self.first_name
        )

        # Wait for employee row
        employee_row.wait_for(
            state="visible",
            timeout=15000
        )

        self.log(
            f"READ - Employee found successfully: "
            f"{self.first_name}"
        )

        # Take screenshot after search
        Screenshot.take(
            self.page,
            "Open Page Update Data User",
            wait_for=employee_row,
            timeout=15000
        )

    # ==========================================================
    # CLICK UPDATE
    # ==========================================================

    def click_update(self):

        self.log(
            "UPDATE - Opening employee edit page"
        )

        # Locate employee row
        row = self.page.locator(
            ".oxd-table-row"
        ).filter(
            has_text=self.first_name
        )

        # Click Edit button
        row.locator(
            "button"
        ).first.click()

        self.log(
            "UPDATE - Edit button clicked"
        )

        # Locate Last Name field
        lastname = self.page.locator(
            "input[name='lastName']"
        )

        # Wait until Last Name field is visible
        expect(
            lastname
        ).to_be_visible(
            timeout=15000
        )

        self.log(
            "UPDATE - Employee edit page opened successfully"
        )

    # ==========================================================
    # UPDATE EMPLOYEE
    # ==========================================================

    def update_employee(self):

        self.log(
            f"UPDATE - Changing last name from "
            f"{self.last_name} to {self.new_last_name}"
        )

        # Locate Last Name field
        lastname = self.page.locator(
            "input[name='lastName']"
        )

        # Clear existing Last Name
        lastname.clear()

        # Fill new Last Name
        lastname.fill(
            self.new_last_name
        )

        self.log(
            "UPDATE - New last name entered"
        )

        # Take screenshot before update
        Screenshot.take(
            self.page,
            "Complete Input Data for Update User",
            wait_for=[
                self.page.get_by_role(
                    "heading",
                    name="Personal Details",
                    exact=True
                ),
                self.page.get_by_text(
                    "Employee Full Name",
                    exact=True
                ),
                self.page.get_by_role(
                    "heading",
                    name="Custom Fields",
                    exact=True
                ),
                self.page.get_by_role(
                    "heading",
                    name="Attachments",
                    exact=True
                )
            ],
            timeout=30000
        )

        self.log(
            "UPDATE - Clicking Save button"
        )

        # Click Save button
        self.page.get_by_role(
            "button",
            name="Save"
        ).first.click()

        # Take screenshot after update
        Screenshot.take(
            self.page,
            "Success Update User",
            wait_for=[
                self.page.get_by_role(
                    "heading",
                    name="Personal Details",
                    exact=True
                ),
                self.page.get_by_text(
                    "Employee Full Name",
                    exact=True
                ),
                self.page.get_by_role(
                    "heading",
                    name="Custom Fields",
                    exact=True
                ),
                self.page.get_by_role(
                    "heading",
                    name="Attachments",
                    exact=True
                )
            ],
            timeout=30000
        )

        self.log(
            f"UPDATE - Employee updated successfully: "
            f"{self.first_name} {self.middle_name} "
            f"{self.new_last_name}"
        )

    # ==========================================================
    # DELETE EMPLOYEE
    # ==========================================================

    def delete_employee(self):

        self.log(
            f"DELETE - Starting deletion for employee: "
            f"{self.first_name}"
        )

        # Search employee
        self.search_employee()

        # Locate employee row
        row = self.page.locator(
            ".oxd-table-row"
        ).filter(
            has_text=self.first_name
        )

        expect(
            row
        ).to_be_visible(
            timeout=15000
        )

        self.log(
            "DELETE - Employee found for deletion"
        )

        # Click Delete button
        row.locator(
            "button"
        ).nth(1).click()

        self.log(
            "DELETE - Delete button clicked"
        )

        # Locate Delete confirmation button
        delete_button = self.page.get_by_role(
            "button",
            name="Yes, Delete"
        )

        # Wait until confirmation dialog is visible
        expect(
            delete_button
        ).to_be_visible(
            timeout=15000
        )

        self.log(
            "DELETE - Delete confirmation dialog displayed"
        )

        # Take screenshot of delete confirmation
        Screenshot.take(
            self.page,
            "Pop Up Confirmation Delete Data User",
            wait_for=delete_button,
            timeout=15000
        )

        # Confirm deletion
        delete_button.click()

        self.log(
            "DELETE - Confirmed employee deletion"
        )

        # Waiting delete completed
        pim_heading = self.page.get_by_role(
            "heading",
            name="PIM",
            exact=True
        )

        expect(
            pim_heading
        ).to_be_visible(
            timeout=30000
        )

        self.log(
            "DELETE - Returned to PIM page"
        )

        # ======================================================
        # VERIFY EMPLOYEE NO LONGER EXISTS
        # ======================================================

        employee_row = self.page.locator(
            ".oxd-table-row"
        ).filter(
            has_text=self.first_name
        )

        expect(
            employee_row
        ).to_have_count(
            0,
            timeout=15000
        )

        self.log(
            f"DELETE - Employee deleted successfully: "
            f"{self.first_name}"
        )

        # Take screenshot after deletion
        Screenshot.take(
            self.page,
            "Success Delete User",
            wait_for=pim_heading,
            timeout=15000
        )