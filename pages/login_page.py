
import allure
from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self):
        self.page.get_by_role("textbox", name="Username").fill("Admin")
        self.page.get_by_role("textbox", name="Password").fill("admin123")
        allure.attach(
            self.page.screenshot(),
            name="Login form with credentials entered",
            attachment_type=allure.attachment_type.PNG,
        )
        self.page.get_by_role("button", name="Login").click()

    def verify_dashboard(self):
        expect(self.page.get_by_text("Dashboard", exact=True).first).to_be_visible()
        allure.attach(
            self.page.screenshot(),
            name="Dashboard after successful login",
            attachment_type=allure.attachment_type.PNG,
        )
