import traceback

import pytest
import allure

from Pages.login_page import LoginPage
from Utils.logGen import LogGen
from Utils.config import (
    ORANGEHRM_USERNAME,
    ORANGEHRM_PASSWORD,
    validate_config
)


logger = LogGen.logger()


# =========================================================
# POSITIVE LOGIN
# =========================================================

@allure.title("Positive Login - Valid Credentials")
def test_positive_login(page):

    test_name = "Positive Login"

    try:

        # =================================================
        # VALIDATE CONFIGURATION
        # =================================================

        validate_config()

        # =================================================
        # GET CREDENTIALS
        # =================================================

        username = ORANGEHRM_USERNAME
        password = ORANGEHRM_PASSWORD

        # =================================================
        # INITIALIZE PAGE OBJECT
        # =================================================

        login = LoginPage(
            page,
            logger
        )

        # =================================================
        # POSITIVE LOGIN
        # =================================================

        with allure.step(
            "Perform positive login"
        ):

            logger.info(
                f"[{test_name}] "
                f"LOGIN - Starting positive login"
            )

            login.positive_login(
                username,
                password
            )

        # =================================================
        # VERIFY LOGIN SUCCESS
        # =================================================

        with allure.step(
            "Verify successful login"
        ):

            logger.info(
                f"[{test_name}] "
                f"LOGIN - Dashboard successfully displayed"
            )

        # =================================================
        # PASS
        # =================================================

        LogGen.pass_test(
            logger,
            test_name
        )

    except Exception as e:

        LogGen.fail_test(
            logger,
            test_name
        )

        logger.error(
            f"ERROR MESSAGE: {str(e)}"
        )

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

        logger.error(
            "FULL TRACEBACK:"
        )

        logger.error(
            traceback.format_exc()
        )

        raise


# =========================================================
# NEGATIVE LOGIN
# =========================================================

@pytest.mark.parametrize(
    "username, password, test_name",
    [
        (
            ORANGEHRM_USERNAME,
            "password_salah",
            "Negative Login - Invalid Password"
        ),
        (
            "username_salah",
            ORANGEHRM_PASSWORD,
            "Negative Login - Invalid Username"
        ),
        (
            "username_salah",
            "password_salah",
            "Negative Login - Invalid Username & Password"
        ),
    ]
)
def test_negative_login(
    page,
    username,
    password,
    test_name
):

    try:

        # =================================================
        # VALIDATE CONFIGURATION
        # =================================================

        validate_config()

        # =================================================
        # ALLURE TITLE
        # =================================================

        allure.dynamic.title(
            test_name
        )

        # =================================================
        # INITIALIZE PAGE OBJECT
        # =================================================

        login = LoginPage(
            page,
            logger
        )

        # =================================================
        # NEGATIVE LOGIN
        # =================================================

        with allure.step(
            f"Perform negative login - {test_name}"
        ):

            logger.info(
                f"[{test_name}] "
                f"LOGIN - Starting negative login"
            )

            # Jangan log password
            logger.info(
                f"[{test_name}] "
                f"Username: {username}"
            )

            login.negative_login(
                username,
                password
            )

        # =================================================
        # VERIFY INVALID CREDENTIALS
        # =================================================

        with allure.step(
            "Verify invalid credentials"
        ):

            logger.info(
                f"[{test_name}] "
                f"LOGIN - Invalid credentials verified"
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

        raise