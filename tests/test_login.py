from Pages.login_page import LoginPage


def test_negative_login(page):

    login = LoginPage(page)

    login.negative_login(
        "Admin",
        "password_salah"
    )


# def test_positive_login(page):
#
#     login = LoginPage(page)
#
#     login.positive_login(
#         "Admin",
#         "admin123"
#     )