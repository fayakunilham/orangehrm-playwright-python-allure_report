from pathlib import Path


class AllureFolder:

    @staticmethod
    def get_next_folder():

        # =================================================
        # ALLURE RESULTS ROOT DIRECTORY
        # =================================================

        allure_root = Path("allure-results")

        # Create allure-results if it does not exist
        allure_root.mkdir(
            parents=True,
            exist_ok=True
        )

        # =================================================
        # GET EXISTING NUMBERED FOLDERS
        # =================================================

        numbers = []

        for folder in allure_root.iterdir():

            if folder.is_dir() and folder.name.isdigit():

                numbers.append(
                    int(folder.name)
                )

        # =================================================
        # DETERMINE NEXT NUMBER
        # =================================================

        next_number = (
            max(numbers) + 1
            if numbers
            else 1
        )

        # =================================================
        # CREATE NEW FOLDER
        # =================================================

        result_folder = (
            allure_root / str(next_number)
        )

        result_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        return result_folder