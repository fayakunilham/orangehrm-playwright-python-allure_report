import pytest
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright

from Pages.login_page import LoginPage


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

        # Hanya membaca file video
        if not file.is_file():
            continue

        if file.suffix.lower() != ".webm":
            continue

        # Format:
        # 1. TestLogin_20260901_140030.webm
        if "." not in file.name:
            continue

        try:

            # Mengambil nomor sebelum titik
            number = int(
                file.name.split(".", 1)[0]
            )

            # Simpan nomor terbesar
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

        # Menjalankan Chromium dalam mode non-headless
        browser = p.chromium.launch(
            headless=False
        )

        # =================================================
        # VIDEO DIRECTORY
        # =================================================

        # Folder utama untuk semua video.
        video_dir = Path("videos")

        # Membuat folder jika belum tersedia.
        video_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        # =================================================
        # CREATE BROWSER CONTEXT
        # =================================================

        # Semua video akan disimpan langsung
        # di folder videos.
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

        # Timeout default untuk action.
        page.set_default_timeout(
            10_000
        )

        # Timeout khusus navigation.
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
        # GET VIDEO FILE
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
            # class TestAdminUserCRUD
            #
            # hasil:
            # TestAdminUserCRUD
            class_name = test_class.__name__

        else:

            # Jika test tidak menggunakan class,
            # gunakan nama test method.
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

            # Mengambil video terbaru
            video_file = max(
                video_files,
                key=lambda file: file.stat().st_mtime
            )

            # Timestamp video
            video_timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            # Nama video:
            #
            # 1. TestAdminUserCRUD_20260901_140958.webm
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
    # INITIALIZE LOGIN PAGE
    # =====================================================

    login_page = LoginPage(page)

    # =====================================================
    # OPEN LOGIN PAGE
    # =====================================================

    login_page.open()

    # =====================================================
    # LOGIN
    # =====================================================

    login_page.positive_login(
        "Admin",
        "admin123"
    )

    # =====================================================
    # RETURN PAGE
    # =====================================================

    return page