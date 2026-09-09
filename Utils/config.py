import os
from dotenv import load_dotenv


load_dotenv()


ORANGEHRM_URL = os.getenv("ORANGEHRM_URL")
ORANGEHRM_USERNAME = os.getenv("ORANGEHRM_USERNAME")
ORANGEHRM_PASSWORD = os.getenv("ORANGEHRM_PASSWORD")


def validate_config():

    assert ORANGEHRM_URL, (
        "ORANGEHRM_URL environment variable "
        "is not configured"
    )

    assert ORANGEHRM_USERNAME, (
        "ORANGEHRM_USERNAME environment variable "
        "is not configured"
    )

    assert ORANGEHRM_PASSWORD, (
        "ORANGEHRM_PASSWORD environment variable "
        "is not configured"
    )