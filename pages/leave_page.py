# import time

# from playwright.sync_api import Page, expect
# import pytest


# class LeavePage:
#     def __init__(self, page:Page):
#         self.page = page

#     def open_leave(self):
#         self.page.locator("//a[contains(@href, 'viewLeaveModule')]").click()

#     def apply_tab(self):
#         self.page.locator('a').filter(has_text='Apply').click()

#         not_found = self.page.get_by_text("No Leave Types with Leave Balance", exact=True)
#         expect(not_found).to_be_visible()
#         pytest.exit()
           


#     def apply_leave(self):
#         self.page.locator("label:has-text('Leave Type')").locator("xpath=following::div[contains(@class,'oxd-select-text')][1]").click()

#         self.page.locator("//label[text()='From Date']/parent::div/following-sibling::div//input").fill("2026-10-26")
#         self.page.locator("//label[text()='To Date']/parent::div/following-sibling::div//input").fill("2026-10-26")

#         self.page.get_by_role('button', name="Apply").click()

#     def verify_leave(self):
#         expect(self.page.get_by_text("Successfully Saved", exact=True)).to_be_visible(timeout=15000)     

#         self.page.locator('a').filter(has_text='My Leave').click()

#         expect(self.page.get_by_role("row", name="CAN - Vacation").locator('label')).to_be_visible()
#         #expect(self.page.locator("div").filter(has_text="CAN - Vacation")).to_be_visible()

#     # def add_comment(self): 
