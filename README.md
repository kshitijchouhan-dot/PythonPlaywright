# Pytest-BDD Playwright framework

## Allure reports

Install the project dependencies and run the tests from this directory:

```powershell
python -m pip install -r requirements.txt
pytest
```

Each pytest run clears the previous `allure-results` and `allure-report`,
then generates fresh results and an HTML report. Failure screenshots are
stored as Allure attachments and are refreshed with the results. Each test
also gets a new Playwright browser context, so cookies and other browser
storage are not carried over between tests.

The `allure-pytest-bdd` integration includes feature names, scenarios, and
individual Gherkin steps in the Allure report. Login flows also attach a
screenshot after the credentials are entered and another after the dashboard
is verified.

The test run uses the Allure command-line tool to generate the report. Install
it from the [official Allure 2 releases](https://github.com/allure-framework/allure2/releases)
and add the extracted `bin` directory to your user `PATH`. Allure also requires
Java. If `JAVA_HOME` is set, it must point to the JDK root directory (not its
`bin` subdirectory).

Open a new terminal and verify the installation:

```powershell
allure --version
allure open allure-report
```

Use `allure`, not `allurew`. Failed tests with an available Playwright `page`
include a screenshot attachment in the Allure report.
