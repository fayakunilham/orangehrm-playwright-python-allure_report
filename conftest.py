import os
import pytest
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from Pages.login_page import LoginPage


# =========================================================
# PROJECT CONFIGURATION
# =========================================================

# Root directory project
BASE_DIR = Path(__file__).resolve().parent

# .env location
ENV_FILE = BASE_DIR / ".env"

# Load environment variables
load_dotenv(ENV_FILE)


# =========================================================
# HELPER - GET NEXT VIDEO NUMBER
# =========================================================

def get_next_video_number(video_dir):

    # Jika folder belum ada
    if not video_dir.exists():
        return 1

    # Menyimpan nomor video terbesar
    max_number = 0

    # Membaca semua file dalam folder videos
    for file in video_dir.iterdir():

        # Hanya membaca file
        if not file.is_file():
            continue

        # Hanya membaca file .webm
        if file.suffix.lower() != ".webm":
            continue

        # Format filename:
        #
        # 1. TestLogin_20260901_140030.webm
        #
        # Ambil bagian sebelum "."
        if "." not in file.name:
            continue

        try:

            number = int(
                file.name.split(".", 1)[0]
            )

            max_number = max(
                max_number,
                number
            )

        except ValueError:
            continue

    # Nomor video berikutnya
    return max_number + 1


# =========================================================
# PAGE FIXTURE
# =========================================================

@pytest.fixture
def page(request):

    # =====================================================
    # START PLAYWRIGHT
    # =====================================================

    with sync_playwright() as p:

        # =================================================
        # LAUNCH BROWSER
        # =================================================

        browser = p.chromium.launch(
            headless=False
        )

        # =================================================
        # VIDEO DIRECTORY
        # =================================================

        video_dir = BASE_DIR / "videos"

        video_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        # =================================================
        # CREATE BROWSER CONTEXT
        # =================================================

        context = browser.new_context(
            record_video_dir=str(video_dir)
        )

        # =================================================
        # CREATE PAGE
        # =================================================

        page = context.new_page()

        # =================================================
        # PLAYWRIGHT TIMEOUT
        # =================================================

        page.set_default_timeout(
            10_000
        )

        page.set_default_navigation_timeout(
            30_000
        )

        # =================================================
        # RUN TEST
        # =================================================

        yield page

        # =================================================
        # CLOSE CONTEXT
        # =================================================

        # Context harus ditutup terlebih dahulu
        # agar video selesai dibuat.
        context.close()

        # =================================================
        # GET VIDEO FILES
        # =================================================

        video_files = list(
            video_dir.glob("*.webm")
        )

        # =================================================
        # GET TEST CLASS NAME
        # =================================================

        test_class = request.node.cls

        if test_class:

            # Contoh:
            #
            # class TestAdminUserCRUD
            #
            # hasil:
            #
            # TestAdminUserCRUD

            class_name = test_class.__name__

        else:

            # Jika test tidak menggunakan class,
            # gunakan nama test.
            class_name = request.node.name

        # =================================================
        # GET NEXT VIDEO NUMBER
        # =================================================

        video_number = get_next_video_number(
            video_dir
        )

        # =================================================
        # RENAME VIDEO
        # =================================================

        if video_files:

            # Ambil video terbaru
            video_file = max(
                video_files,
                key=lambda file: file.stat().st_mtime
            )

            # Timestamp
            video_timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            # Nama video:
            #
            # 1. TestLogin_20260908_141500.webm

            video_name = (
                f"{video_number}. "
                f"{class_name}_"
                f"{video_timestamp}.webm"
            )

            # Rename video
            video_file.rename(
                video_dir / video_name
            )

        # =================================================
        # CLOSE BROWSER
        # =================================================

        browser.close()


# =========================================================
# LOGGED IN PAGE FIXTURE
# =========================================================

@pytest.fixture
def logged_in_page(page):

    # =====================================================
    # GET CREDENTIALS FROM .ENV
    # =====================================================

    username = os.getenv(
        "ORANGEHRM_USERNAME"
    )

    password = os.getenv(
        "ORANGEHRM_PASSWORD"
    )

    # =====================================================
    # VALIDATE ENVIRONMENT VARIABLES
    # =====================================================

    assert username, (
        "ORANGEHRM_USERNAME environment variable "
        "is not configured"
    )

    assert password, (
        "ORANGEHRM_PASSWORD environment variable "
        "is not configured"
    )

    # =====================================================
    # INITIALIZE LOGIN PAGE
    # =====================================================

    login_page = LoginPage(
        page
    )

    # =====================================================
    # OPEN LOGIN PAGE
    # =====================================================

    login_page.open()

    # =====================================================
    # LOGIN
    # =====================================================

    login_page.positive_login(
        username,
        password
    )

    # =====================================================
    # RETURN LOGGED-IN PAGE
    # =====================================================

    return page
