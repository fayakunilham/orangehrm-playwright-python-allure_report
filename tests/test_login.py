import traceback
import allure

from Pages.login_page import LoginPage
from Utils.logGen import LogGen


logger = LogGen.logger()


@allure.title("Negative Login - Invalid Credentials")
def test_negative_login(page):

    test_name = "Negative Login"

    try:

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

        with allure.step("Perform negative login"):

            logger.info(
                f"[{test_name}] "
                f"LOGIN - Starting negative login"
            )

            login.negative_login(
                "Admin",
                "password_salah"
            )

        # =================================================
        # VERIFY INVALID CREDENTIALS
        # =================================================

        with allure.step("Verify invalid credentials"):

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

    # # =====================================================
    # # START TEST
    # # =====================================================
    #
    # LogGen.start_test(
    #     logger,
    #     test_name
    # )



# =========================================================
# POSITIVE LOGIN
# =========================================================

# def test_positive_login(page):
#
#     test_name = "Positive Login"
#
#     LogGen.start_test(
#         logger,
#         test_name
#     )
#
#     try:
#
#         login = LoginPage(
#             page,
#             logger
#         )
#
#         logger.info(
#             f"[{test_name}] "
#             f"LOGIN - Starting positive login"
#         )
#
#         login.positive_login(
#             "Admin",
#             "admin123"
#         )
#
#         logger.info(
#             f"[{test_name}] "
#             f"LOGIN - Login successful"
#         )
#
#         LogGen.pass_test(
#             logger,
#             test_name
#         )
#
#     except Exception as e:
#
#         LogGen.fail_test(
#             logger,
#             test_name
#         )
#
#         logger.error(
#             f"ERROR MESSAGE: {str(e)}"
#         )
#
#         logger.error(
#             "FULL TRACEBACK:"
#         )
#
#         logger.error(
#             traceback.format_exc()
#         )
#
#         raise


# def test_positive_login(page):
#
#     login = LoginPage(page)
#
#     login.positive_login(
#         "Admin",
#         "admin123"
#     )