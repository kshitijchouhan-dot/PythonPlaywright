import time

from playwright.sync_api import Page,expect


class AdminPage:
    def __init__(self, page:Page):
        self.page = page

    def open_admin(self):
        self.page.locator("//a[contains(@href, 'viewAdminModule')]").click()

        expect(
            self.page.get_by_role("heading", name="System Users")
        ).to_be_visible()

    def add_user(self):
        self.page.get_by_role("button", name="Add").click()

        expect(
            self.page.get_by_role("heading", name="Add User")
        ).to_be_visible()

        # Select User Role
        self.page.locator("label:has-text('User Role')").locator("xpath=following::div[contains(@class,'oxd-select-text')][1]").click()
        self.page.get_by_role("option", name="Admin").click()
        
        # Select Employee
        employee = self.page.get_by_placeholder("Type for hints...")
        employee.fill("Charles  Carter")
        time.sleep(3)
        option = self.page.get_by_role("option").first
        expect(option).to_be_visible()
        option.click()

        # Select Status
        self.page.locator(
            "label:has-text('Status')"
        ).locator("xpath=following::div[contains(@class,'oxd-select-text')][1]").click()
        self.page.get_by_text("Enabled", exact=True).click()

        # Enter user details
        self.page.locator("//label[text()='Username']/parent::div/following-sibling::div/input").fill("Aadi Dhamal")
        self.page.locator("//label[text()='Password']/parent::div/following-sibling::div/input").fill("Test@12345")
        self.page.locator("//label[text()='Confirm Password']/parent::div/following-sibling::div/input").fill("Test@12345")

        self.page.get_by_role("button", name="Save").click()

        expect(
            self.page.get_by_role("heading", name="System Users")
        ).to_be_visible(timeout=20000)

    def verify_user(self):
        self.page.locator("//label[text()='Username']/parent::div/following-sibling::div/input").fill("Aadi Dhamal")
        self.page.get_by_role("button", name="Search").click()

        expect(
            self.page.get_by_role("cell", name="Aadi Dhamal", exact=True)
        ).to_be_visible(timeout=15000)

    def edit_user(self):
        self.page.get_by_role("cell", name="Aadi Dhamal", exact=True)
        self.page.get_by_role("row", name="Aadi Dhamal").locator('label').click()
        # Edit Button
        time.sleep(3)
        self.page.locator(".oxd-icon.bi-pencil-fill").click()
        # Edit User Role
        self.page.locator("label:has-text('User Role')").locator("xpath=following::div[contains(@class,'oxd-select-text')][1]").click()
        self.page.get_by_role("option", name="ESS").click()
        # Edit Username
        self.page.locator("//label[text()='Username']/parent::div/following-sibling::div/input").fill("Venom Boy")
        # Save Button
        time.sleep(3)
        self.page.get_by_role('button', name='Save').click()
        # Verify save details
        expect(
                    self.page.get_by_text("Successfully Updated", exact=True)
              ).to_be_visible(timeout=15000)


    def delete_user(self):

        username = self.page.locator("//label[text()='Username']/parent::div/following-sibling::div/input")
        username.fill("")
        username.fill("Venom Boy")
        
        self.page.get_by_role("button", name="Search").click()

        row = self.page.get_by_role("row").filter(
             has=self.page.get_by_role("cell", name="Venom Boy", exact=True)
        )
        expect(row).to_be_visible(timeout=15000)
        self.page.get_by_role("row", name="Venom Boy").locator('label').click()
        time.sleep(3)
        self.page.get_by_role('button', name="Delete Selected").click()
        self.page.get_by_role('button', name='Yes, Delete').click()
    
    def verify_user_deleted(self):

        expect(
            self.page.get_by_text("Successfully Deleted", exact=True)
        ).to_be_visible(timeout=15000)

