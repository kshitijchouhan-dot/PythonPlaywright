
from pytest_bdd import scenarios, given, when, then

from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage

scenarios("../features/recruitment.feature")


@given("I am logged into OrangeHRM")
def login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login()
    login_page.verify_dashboard()
    
@given("Navigate to Recruitment Page")
def navigate_admin(page):
    RecruitmentPage(page).open_recruitment()

@when("Add Candidates details")
def add_candidate(page):
    RecruitmentPage(page).add_candidate()

@when("Shortlist the candidate") 
def shortlist_candidate(page):
    RecruitmentPage(page).shortlist_candidate()

@then("Verify the candidate and status")
def verify_candidate_status(page):
    RecruitmentPage(page).verify_candidate_status()

@then("Schedule the Interview of candidate and verify")
def schedule_interview(page):
    RecruitmentPage(page).schedule_interview()

@then("Marked the candidate passed and verify")
def interview_passed(page):
    RecruitmentPage(page).interview_passed()
    