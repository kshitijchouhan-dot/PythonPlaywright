

import os
import shutil
import subprocess
from pathlib import Path

import pytest
import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright

PROJECT_DIR = Path(__file__).parent
ALLURE_REPORT_DIR = PROJECT_DIR / "allure-report"

BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"


def pytest_sessionstart(session):
    if ALLURE_REPORT_DIR.exists():
        shutil.rmtree(ALLURE_REPORT_DIR)


def pytest_sessionfinish(session, exitstatus):
    command = [
        "allure",
        "generate",
        "allure-results",
        "--clean",
        "-o",
        "allure-report",
    ]
    if os.name == "nt":
        command = [os.environ.get("COMSPEC", "cmd.exe"), "/c", *command]
    subprocess.run(command, cwd=PROJECT_DIR, check=True)


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.set_default_timeout(15000)

    yield page

    context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        page = item.funcargs.get("page")
        if page is not None and not page.is_closed():
            allure.attach(
                page.screenshot(),
                name=f"Failure screenshot ({report.when})",
                attachment_type=AttachmentType.PNG,
            )