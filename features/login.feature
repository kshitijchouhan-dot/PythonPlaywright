
Feature: OrangeHRM Login

  Scenario: Login with valid credentials
    Given I open the OrangeHRM login page
    When I enter valid login credentials
    Then I should see the dashboard
