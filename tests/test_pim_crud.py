from Pages.login_page import LoginPage
from Pages.pim_page import EmployeePage


def test_employee_crud(page):

    login = LoginPage(page)
    employee = EmployeePage(page)

    login.positive_login("Admin", "admin123")

    # CREATE
    employee.click_add()
    employee.create_employee()

    # READ
    employee.search_employee()

    # UPDATE
    employee.click_update()
    employee.update_employee()

    # DELETE
    employee.delete_employee()