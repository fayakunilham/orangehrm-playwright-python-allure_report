import allure
import traceback

from Pages.login_page import LoginPage
from Pages.admin_page import AdminPage
from Pages.pim_page import EmployeePage
from Utils.logGen import LogGen


logger = LogGen.logger()


@allure.title("Admin - User CRUD")
@allure.description(
    "Verify Create, Read, Update and Delete User"
)
def test_admin_user_crud(page):

    test_name = "Admin - User CRUD"

    # =====================================================
    # START TEST
    # =====================================================

    LogGen.start_test(
        logger,
        test_name
    )

    try:

        # =================================================
        # INITIALIZE PAGE OBJECT
        # =================================================

        login = LoginPage(page)
        admin = AdminPage(page)
        employee = EmployeePage(page)

        # =================================================
        # LOGIN
        # =================================================

        with allure.step("Login to OrangeHRM"):

            logger.info(
                f"[{test_name}] "
                f"LOGIN - Starting login"
            )

            login.positive_login(
                "Admin",
                "admin123"
            )

            logger.info(
                f"[{test_name}] "
                f"LOGIN - Login successful"
            )

        # =================================================
        # OPEN PIM
        # =================================================

        with allure.step("Open PIM Menu"):

            logger.info(
                f"[{test_name}] "
                f"PIM - Opening PIM menu"
            )

            employee.click_add()

            logger.info(
                f"[{test_name}] "
                f"PIM - PIM menu opened"
            )

        # =================================================
        # CREATE EMPLOYEE
        # =================================================

        with allure.step("Create Employee"):

            logger.info(
                f"[{test_name}] "
                f"CREATE EMPLOYEE - Starting"
            )

            employee.create_employee()

            employee_name = (
                f"{employee.first_name} "
                f"{employee.middle_name} "
                f"{employee.last_name}"
            )

            logger.info(
                f"[{test_name}] "
                f"CREATE EMPLOYEE - "
                f"Created: {employee_name}"
            )

        # =================================================
        # OPEN ADMIN
        # =================================================

        with allure.step("Open Admin Menu"):

            logger.info(
                f"[{test_name}] "
                f"ADMIN - Opening Admin menu"
            )

            admin.open_admin()

            logger.info(
                f"[{test_name}] "
                f"ADMIN - Admin menu opened"
            )

        # =================================================
        # CREATE USER
        # =================================================

        with allure.step("Create New User"):

            logger.info(
                f"[{test_name}] "
                f"CREATE USER - "
                f"Creating user for "
                f"{employee_name}"
            )

            admin.click_add()

            admin.create_user(
                employee_name
            )

            logger.info(
                f"[{test_name}] "
                f"CREATE USER - "
                f"User created successfully"
            )

        # =================================================
        # READ
        # =================================================

        with allure.step("Search Created User"):

            logger.info(
                f"[{test_name}] "
                f"READ - Searching user"
            )

            admin.search_created_user()

            logger.info(
                f"[{test_name}] "
                f"READ - "
                f"User found successfully"
            )

        # =================================================
        # UPDATE
        # =================================================

        with allure.step("Update User"):

            logger.info(
                f"[{test_name}] "
                f"UPDATE - Opening edit page"
            )

            admin.edit_user()

            logger.info(
                f"[{test_name}] "
                f"UPDATE - "
                f"Edit page opened"
            )

            logger.info(
                f"[{test_name}] "
                f"UPDATE - Updating user"
            )

            admin.update_user()

            logger.info(
                f"[{test_name}] "
                f"UPDATE - "
                f"User updated successfully"
            )

        # =================================================
        # DELETE
        # =================================================

        with allure.step("Delete User"):

            logger.info(
                f"[{test_name}] "
                f"DELETE - Deleting user"
            )

            admin.delete_user()

            logger.info(
                f"[{test_name}] "
                f"DELETE - "
                f"User deleted successfully"
            )

        # =================================================
        # PASS
        # =================================================

        LogGen.pass_test(
            logger,
            test_name
        )

    except Exception as e:

        # =================================================
        # FAIL
        # =================================================

        LogGen.fail_test(
            logger,
            test_name
        )

        logger.error(
            f"ERROR MESSAGE: {str(e)}"
        )

        # -------------------------------------------------
        # ERROR LOCATION
        # -------------------------------------------------

        error_trace = traceback.extract_tb(
            e.__traceback__
        )

        if error_trace:

            last_error = error_trace[-1]

            logger.error(
                f"ERROR LOCATION: "
                f"{last_error.filename}:"
                f"{last_error.lineno}"
            )

            logger.error(
                f"ERROR FUNCTION: "
                f"{last_error.name}"
            )

            logger.error(
                f"ERROR CODE: "
                f"{last_error.line}"
            )

        # -------------------------------------------------
        # FULL TRACEBACK
        # -------------------------------------------------

        logger.error(
            "FULL TRACEBACK:"
        )

        logger.error(
            traceback.format_exc()
        )

        # Important:
        # Re-raise exception so pytest marks test as FAILED
        raise