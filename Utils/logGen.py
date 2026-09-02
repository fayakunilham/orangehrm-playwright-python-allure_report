import logging
import os

from datetime import datetime


class LogGen:

    # =====================================================
    # GLOBAL TEST COUNTER
    # =====================================================

    total_tests = 0
    passed_tests = 0
    failed_tests = 0

    # =====================================================
    # TEST EXECUTION TIME
    # =====================================================

    execution_start_time = None
    execution_end_time = None

    # =====================================================
    # LOGGER
    # =====================================================

    @staticmethod
    def logger():

        # -------------------------------------------------
        # CREATE LOG DIRECTORY
        # -------------------------------------------------

        log_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "Logs"
        )

        os.makedirs(
            log_dir,
            exist_ok=True
        )

        # -------------------------------------------------
        # CREATE ONE LOG FILE
        # -------------------------------------------------

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        log_file = os.path.join(
            log_dir,
            f"test_{timestamp}.log"
        )

        # -------------------------------------------------
        # CREATE LOGGER
        # -------------------------------------------------

        logger = logging.getLogger(
            "playwright_test_logger"
        )

        logger.setLevel(
            logging.INFO
        )

        # -------------------------------------------------
        # PREVENT DUPLICATE HANDLER
        # -------------------------------------------------

        if not logger.handlers:

            file_handler = logging.FileHandler(
                log_file,
                encoding="utf-8"
            )

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )

            file_handler.setFormatter(
                formatter
            )

            logger.addHandler(
                file_handler
            )

        # -------------------------------------------------
        # PREVENT LOG PROPAGATION
        # -------------------------------------------------

        logger.propagate = False

        # -------------------------------------------------
        # RESET TEST DATA
        # -------------------------------------------------

        LogGen.total_tests = 0
        LogGen.passed_tests = 0
        LogGen.failed_tests = 0

        LogGen.execution_start_time = datetime.now()
        LogGen.execution_end_time = None

        return logger

    # =====================================================
    # START TEST
    # =====================================================

    @staticmethod
    def start_test(logger, test_name):

        # -------------------------------------------------
        # START TIME
        # -------------------------------------------------

        start_time = datetime.now()

        # -------------------------------------------------
        # SAVE START TIME TO LOGGER
        # -------------------------------------------------

        logger.start_time = start_time

        # -------------------------------------------------
        # INCREASE TOTAL TEST
        # -------------------------------------------------

        LogGen.total_tests += 1

        # -------------------------------------------------
        # HEADER
        # -------------------------------------------------

        logger.info("")

        logger.info(
            "=" * 80
        )

        logger.info(
            "TEST EXECUTION START".center(80)
        )

        logger.info(
            "=" * 80
        )

        logger.info(
            f"TEST NAME  : {test_name}"
        )

        logger.info(
            f"START TIME : "
            f"{start_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        logger.info(
            "STATUS     : STARTED"
        )

        logger.info(
            "-" * 80
        )

    # =====================================================
    # PASS TEST
    # =====================================================

    @staticmethod
    def pass_test(logger, test_name):

        # -------------------------------------------------
        # FINISH TIME
        # -------------------------------------------------

        finish_time = datetime.now()

        # -------------------------------------------------
        # CALCULATE DURATION
        # -------------------------------------------------

        duration = (
            finish_time - logger.start_time
        ).total_seconds()

        # -------------------------------------------------
        # INCREASE PASSED COUNTER
        # -------------------------------------------------

        LogGen.passed_tests += 1

        # -------------------------------------------------
        # RESULT
        # -------------------------------------------------

        logger.info(
            "-" * 80
        )

        logger.info(
            f"TEST NAME   : {test_name}"
        )

        logger.info(
            "RESULT      : PASSED"
        )

        logger.info(
            f"FINISH TIME : "
            f"{finish_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        logger.info(
            f"DURATION    : "
            f"{duration:.2f} seconds"
        )

        # -------------------------------------------------
        # FOOTER
        # -------------------------------------------------

        logger.info(
            "=" * 80
        )

        logger.info(
            "TEST EXECUTION END".center(80)
        )

        logger.info(
            "=" * 80
        )

        logger.info("")

    # =====================================================
    # FAIL TEST
    # =====================================================

    @staticmethod
    def fail_test(logger, test_name):

        # -------------------------------------------------
        # FINISH TIME
        # -------------------------------------------------

        finish_time = datetime.now()

        # -------------------------------------------------
        # CALCULATE DURATION
        # -------------------------------------------------

        duration = (
            finish_time - logger.start_time
        ).total_seconds()

        # -------------------------------------------------
        # INCREASE FAILED COUNTER
        # -------------------------------------------------

        LogGen.failed_tests += 1

        # -------------------------------------------------
        # RESULT
        # -------------------------------------------------

        logger.info(
            "-" * 80
        )

        logger.info(
            f"TEST NAME   : {test_name}"
        )

        logger.info(
            "RESULT      : FAILED"
        )

        logger.info(
            f"FINISH TIME : "
            f"{finish_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        logger.info(
            f"DURATION    : "
            f"{duration:.2f} seconds"
        )

        # -------------------------------------------------
        # FOOTER
        # -------------------------------------------------

        logger.info(
            "=" * 80
        )

        logger.info(
            "TEST EXECUTION END".center(80)
        )

        logger.info(
            "=" * 80
        )

        logger.info("")

    # =====================================================
    # EXECUTION SUMMARY
    # =====================================================

    @staticmethod
    def summary(logger):

        # -------------------------------------------------
        # EXECUTION END TIME
        # -------------------------------------------------

        LogGen.execution_end_time = datetime.now()

        # -------------------------------------------------
        # CALCULATE EXECUTION DURATION
        # -------------------------------------------------

        if LogGen.execution_start_time:

            execution_duration = (
                LogGen.execution_end_time
                - LogGen.execution_start_time
            ).total_seconds()

        else:

            execution_duration = 0

        # -------------------------------------------------
        # CALCULATE PASS RATE
        # -------------------------------------------------

        if LogGen.total_tests > 0:

            pass_rate = (
                LogGen.passed_tests
                / LogGen.total_tests
            ) * 100

        else:

            pass_rate = 0

        # -------------------------------------------------
        # SUMMARY HEADER
        # -------------------------------------------------

        logger.info("")

        logger.info(
            "=" * 80
        )

        logger.info(
            "TEST EXECUTION SUMMARY".center(80)
        )

        logger.info(
            "=" * 80
        )

        # -------------------------------------------------
        # SUMMARY RESULT
        # -------------------------------------------------

        logger.info(
            f"TOTAL TEST CASE : "
            f"{LogGen.total_tests}"
        )

        logger.info(
            f"PASSED          : "
            f"{LogGen.passed_tests}"
        )

        logger.info(
            f"FAILED          : "
            f"{LogGen.failed_tests}"
        )

        logger.info(
            f"PASS RATE       : "
            f"{pass_rate:.2f}%"
        )

        logger.info(
            f"EXECUTION START : "
            f"{LogGen.execution_start_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        logger.info(
            f"EXECUTION END   : "
            f"{LogGen.execution_end_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        logger.info(
            f"TOTAL DURATION  : "
            f"{execution_duration:.2f} seconds"
        )

        # -------------------------------------------------
        # SUMMARY FOOTER
        # -------------------------------------------------

        logger.info(
            "=" * 80
        )

        logger.info(
            "TEST EXECUTION FINISHED".center(80)
        )

        logger.info(
            "=" * 80
        )

        logger.info("")