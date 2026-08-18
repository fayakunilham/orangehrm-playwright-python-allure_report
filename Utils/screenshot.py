from datetime import datetime
from pathlib import Path


class Screenshot:

    @staticmethod
    def take(page, filename):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        screenshot_dir = Path("Screenshots")
        screenshot_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        page.screenshot(
            path=screenshot_dir / f"{filename}_{timestamp}.png",
            full_page=True
        )