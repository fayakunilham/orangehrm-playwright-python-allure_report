import traceback
import allure

from Pages.login_page import LoginPage
from Pages.pim_page import EmployeePage
from Utils.logGen import LogGen


# =========================================================
# ALLURE TEST INFORMATION
# =========================================================

@allure.epic("Employee Management")
@allure.feature("Employee CRUD")
@allure.story("Create, Read, Update, Delete Employee")
@allure.title("Employee CRUD - Create, Read, Update, Delete")
@allure.description(
    "Verify that an employee can be created, searched, updated, "
    "and deleted successfully."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_employee_crud(page):

    # =====================================================
    # INITIALIZE LOGGER
    # =====================================================

    logger = LogGen.logger()

    test_name = "Employee - CRUD"

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

        login = LoginPage(
            page,
            logger
        )

        employee = EmployeePage(
            page,
            logger
        )

        # =================================================
        # LOGIN
        # =================================================

        with allure.step("Login with valid credentials"):

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
        # CREATE
        # =================================================

        with allure.step("Create new employee"):

            logger.info(
                f"[{test_name}] "
                f"CREATE - Opening Add Employee page"
            )

            employee.click_add()

            logger.info(
                f"[{test_name}] "
                f"CREATE - Creating employee"
            )

            employee.create_employee()

            employee_name = (
                f"{employee.first_name} "
                f"{employee.middle_name} "
                f"{employee.last_name}"
            )

            logger.info(
                f"[{test_name}] "
                f"CREATE - Employee created: "
                f"{employee_name}"
            )

            # Add employee information to Allure report
            allure.attach(
                employee_name,
                name="Created Employee",
                attachment_type=allure.attachment_type.TEXT
            )

        # =================================================
        # READ
        # =================================================

        with allure.step("Search created employee"):

            logger.info(
                f"[{test_name}] "
                f"READ - Searching employee: "
                f"{employee_name}"
            )

            employee.search_employee()

            logger.info(
                f"[{test_name}] "
                f"READ - Employee found successfully"
            )

        # =================================================
        # UPDATE
        # =================================================

        with allure.step("Update employee"):

            logger.info(
                f"[{test_name}] "
                f"UPDATE - Opening employee edit page"
            )

            employee.click_update()

            logger.info(
                f"[{test_name}] "
                f"UPDATE - Updating employee"
            )

            employee.update_employee()

            logger.info(
                f"[{test_name}] "
                f"UPDATE - Employee updated successfully"
            )

        # =================================================
        # DELETE
        # =================================================

        with allure.step("Delete employee"):

            logger.info(
                f"[{test_name}] "
                f"DELETE - Deleting employee: "
                f"{employee_name}"
            )

            employee.delete_employee()

            logger.info(
                f"[{test_name}] "
                f"DELETE - Employee deleted successfully"
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

        # =================================================
        # ERROR LOCATION
        # =================================================

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

        # =================================================
        # FULL TRACEBACK
        # =================================================

        logger.error(
            "FULL TRACEBACK:"
        )

        logger.error(
            traceback.format_exc()
        )

        # =================================================
        # RE-RAISE
        # =================================================

        raise