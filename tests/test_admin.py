import allure

from Pages.login_page import LoginPage
from Pages.admin_page import AdminPage
from Pages.pim_page import EmployeePage


@allure.title("Admin - User CRUD")
@allure.description(
    "Verify Create, Read, Update and Delete User"
)
def test_admin_user_crud(page):

    login = LoginPage(page)
    admin = AdminPage(page)
    employee = EmployeePage(page)

    # =====================================================
    # LOGIN
    # =====================================================

    with allure.step("Login to OrangeHRM"):

        login.positive_login(
            "Admin",
            "admin123"
        )

    # =====================================================
    # OPEN PIM
    # =====================================================

    with allure.step("Open Pim Menu"):
        employee.click_add()

    # =====================================================
    # CREATE User employee
    # =====================================================

    with allure.step("Create Employee"):
        employee.create_employee()

        employee_name = (
            f"{employee.first_name} "
            f"{employee.middle_name} "
            f"{employee.last_name}"
        )

    # =====================================================
    # OPEN ADMIN
    # =====================================================

    with allure.step("Open Admin menu"):

        admin.open_admin()

    # =====================================================
    # CREATE Admin
    # =====================================================

    with allure.step("Create new user"):

        admin.click_add()
        admin.create_user(employee_name)

    # =====================================================
    # READ
    # =====================================================

    with allure.step("Search created user"):

        admin.search_created_user()

    # =====================================================
    # UPDATE
    # =====================================================

    with allure.step("Update user"):

        admin.edit_user()
        admin.update_user()

    # =====================================================
    # DELETE
    # =====================================================

    with allure.step("Delete user"):

        admin.delete_user()