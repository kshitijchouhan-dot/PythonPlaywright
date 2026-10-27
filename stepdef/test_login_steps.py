
from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage

scenarios("..//features/login.feature")


@given("I open the OrangeHRM login page")
def open_login(page):
    LoginPage(page).open()


@when("I enter valid login credentials")
def enter_credentials(page):
    LoginPage(page).login()


@then("I should see the dashboard")
def verify_dashboard(page):
    LoginPage(page).verify_dashboard()
