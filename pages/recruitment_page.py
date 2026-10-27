import time

from playwright.sync_api import Page,expect


class RecruitmentPage:

    firstname = "Gurpreet"
    lastname = "Singh"
    candidate = f"{firstname} {lastname}"
    email = "king@example.com"
    resume_path = r"C:\Users\kshitij\Downloads\pdf-sample.pdf"
    interview_title = "Senior Associate Interview"
    interviewer_name = "Ranga  Akunuri"

    def __init__(self, page:Page): 
        self.page = page

    def open_recruitment(self):
        self.page.locator("//a[contains(@href, 'viewRecruitmentModule')]").click()

        expect(
            self.page.get_by_role("heading", name="Recruitment")
        ).to_be_visible()

    def add_candidate(self):
        self.page.get_by_role("button", name="Add").click()

        expect(
            self.page.get_by_role("heading", name="Add Candidate")
        ).to_be_visible()

        # Add Candidate Details
        self.page.get_by_placeholder("First Name").fill(self.firstname)
        self.page.get_by_placeholder("Last Name").fill(self.lastname)

        self.page.locator(
                    "label:has-text('Vacancy')"
                ).locator("xpath=following::div[contains(@class,'oxd-select-text')][1]").click()
        self.page.get_by_text("Payroll Administrator", exact=True).click()

        self.page.locator("form").get_by_placeholder("Type here").first.fill(self.email)
        self.page.locator("form input[type='file']").set_input_files(self.resume_path)

        consent_input = self.page.locator("form input[type='checkbox']")
        consent_input.locator("xpath=..").click()
        expect(consent_input).to_be_checked()

        self.page.get_by_role("button", name="Save").click()
        expect(
            self.page.get_by_text("Successfully Saved", exact=True)
        ).to_be_visible(timeout=15000)


    def shortlist_candidate(self):
        self.open_recruitment()
        
        employee = self.page.get_by_placeholder("Type for hints...")
        employee.fill(self.firstname)
        time.sleep(4)
        option = self.page.get_by_role("option").first
        expect(option).to_be_visible()
        option.click()

        self.page.get_by_role("button", name="Search").click()
        
        candidate_row = self.page.get_by_role("row").filter(has_text=self.candidate)
        expect(candidate_row).to_have_count(1, timeout=15000)
        expect(candidate_row).to_be_visible()

        candidate_row.locator(".oxd-icon.bi-eye-fill").click()

        expect(
            self.page.get_by_role("button", name=" Shortlist ")
        ).to_be_visible()

        self.page.get_by_role('button', name=" Shortlist ").click()

        expect(
            self.page.get_by_role("heading", name="Shortlist Candidate")
        ).to_be_visible()

        self.page.get_by_placeholder("Type here").fill(
            "This Candidate has been Selected"
        )
        time.sleep(2)

        self.page.get_by_role("button", name="Save").click()
        expect(
            self.page.get_by_text("Successfully Updated", exact=True)
        ).to_be_visible(timeout=15000)

    def verify_candidate_status(self): 
        # self.open_recruitment()
        
        # employee = self.page.get_by_placeholder("Type for hints...")
        # employee.fill("King")
        # time.sleep(3)
        # option = self.page.get_by_role("option").first
        # expect(option).to_be_visible()
        # option.click()

        # self.page.get_by_role("button", name="Search").click()
        
        # candidate_row = self.page.get_by_role("row").filter(has_text=self.candidate)
        # expect(candidate_row).to_have_count(1, timeout=15000)
        # expect(candidate_row).to_be_visible()

        # candidate_row.locator(".oxd-icon.bi-eye-fill").click()

        expect(
            self.page.get_by_text("Status: Shortlisted", exact=True)
        ).to_be_visible(timeout=15000)

        expect(
            self.page.get_by_role('button', name=
            "Schedule Interview", exact=True)
        ).to_be_visible(timeout=15000)


    def schedule_interview(self):

        self.page.get_by_role('button', name="Schedule Interview").click()

        self.page.locator("label:has-text('Interview Title')").locator(
            "xpath=../following-sibling::div//input"
        ).fill(self.interview_title)

        interviewer_field = self.page.get_by_placeholder("Type for hints...")
        interviewer_field.fill(self.interviewer_name)
        interviewer_option = self.page.get_by_role(
            "option", name=self.interviewer_name, exact=True
        )
        expect(interviewer_option).to_be_visible()
        interviewer_option.click()

        self.page.locator("//label[text()='Date']/parent::div/following-sibling::div//input").fill("2026-10-26")

        self.page.locator('//input[@placeholder="hh:mm"]').fill("02:30 PM")

        self.page.get_by_placeholder("Type here").fill("Please Joined 10 minutes before")

        self.page.get_by_role('button', name="Save").click()

        expect(
                self.page.get_by_text("Successfully Updated", exact=True)
        ).to_be_visible(timeout=15000)

    def interview_passed(self):

        self.page.get_by_role('button', name="Mark Interview Passed").click()

        self.page.get_by_placeholder("Type here").fill("Got Selected")

        self.page.get_by_role('button', name="Save").click()
        expect(
            self.page.get_by_text("Successfully Updated", exact=True)
        ).to_be_visible(timeout=15000)
