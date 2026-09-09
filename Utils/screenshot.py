from pathlib import Path
from datetime import datetime


class Screenshot:

    # =========================================================
    # COUNTER SCREENSHOT
    # =========================================================

    # Counter screenshot untuk satu kali execution
    _counter = 0

    # =========================================================
    # EXECUTION FOLDER
    # =========================================================

    # Folder khusus untuk satu kali execution
    _run_dir = None

    @classmethod
    def take(
            cls,
            page,
            name,
            wait_for=None,
            timeout=15000,
            full_page=True
    ):

        # =====================================================
        # ADD SCREENSHOT NUMBER
        # =====================================================

        # Tambahkan nomor screenshot
        cls._counter += 1

        # =====================================================
        # CREATE EXECUTION FOLDER
        # =====================================================

        # Buat folder execution jika belum dibuat
        if cls._run_dir is None:

            # Timestamp untuk execution
            run_timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            # Folder utama screenshot
            screenshot_root = Path("screenshots")

            # Buat folder utama jika belum ada
            screenshot_root.mkdir(
                parents=True,
                exist_ok=True
            )

            # =================================================
            # FIND LAST EXECUTION NUMBER
            # =================================================

            execution_number = 0

            for folder in screenshot_root.iterdir():

                # Pastikan hanya membaca folder
                if not folder.is_dir():
                    continue

                # Expected format:
                # 1. 20260901_105849
                if "." not in folder.name:
                    continue

                try:

                    number = int(
                        folder.name.split(
                            ".",
                            1
                        )[0]
                    )

                    if number > execution_number:
                        execution_number = number

                except ValueError:

                    continue

            # =================================================
            # CREATE NEXT EXECUTION NUMBER
            # =================================================

            execution_number += 1

            # =================================================
            # CREATE EXECUTION FOLDER
            # =================================================

            cls._run_dir = (
                screenshot_root
                / f"{execution_number}. {run_timestamp}"
            )

            cls._run_dir.mkdir(
                parents=True,
                exist_ok=True
            )

        # =====================================================
        # SCREENSHOT TIMESTAMP
        # =====================================================

        # Timestamp untuk setiap screenshot
        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        # =====================================================
        # CREATE SCREENSHOT NAME
        # =====================================================

        # Format:
        # 1. login_20260901_105850.png
        screenshot_name = (
            f"{cls._counter}. "
            f"{name}_{timestamp}.png"
        )

        # =====================================================
        # FULL SCREENSHOT PATH
        # =====================================================

        screenshot_path = (
            cls._run_dir
            / screenshot_name
        )

        # =====================================================
        # WAIT FOR UI
        # =====================================================

        if wait_for:

            # Jika wait_for berupa list
            if isinstance(
                wait_for,
                list
            ):

                for locator in wait_for:

                    locator.wait_for(
                        state="visible",
                        timeout=timeout
                    )

            # Jika hanya satu locator
            else:

                wait_for.wait_for(
                    state="visible",
                    timeout=timeout
                )

        # =====================================================
        # TAKE SCREENSHOT
        # =====================================================

        page.screenshot(
            path=str(screenshot_path),
            full_page=True
        )

        # =====================================================
        # RETURN SCREENSHOT PATH
        # =====================================================

        return screenshot_path