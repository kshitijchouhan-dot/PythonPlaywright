

from pytest_bdd import scenarios, given, when, then

from pages.login_page import LoginPage
from pages.admin_page import AdminPage

scenarios("../features/admin.feature")


@given("I am logged into OrangeHRM")
def login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login()
    login_page.verify_dashboard()

@given("I navigate to Admin")
def navigate_admin(page):
    AdminPage(page).open_admin()

@when("I create a new user")
def create_user(page):
    AdminPage(page).add_user() 

@then("the user should be displayed in the user list")
def verify_user(page):
    AdminPage(page).verify_user()

@then("edit the user which is created")
def edit_user(page):
    AdminPage(page).edit_user()

@then("delete the user which is created and verify it")
def delete_user_verify(page):
    AdminPage(page).delete_user()
    AdminPage(page).verify_user_deleted()
