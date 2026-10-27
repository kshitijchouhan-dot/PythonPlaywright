
Feature: OrangeHRM Admin

  Scenario: Add a new user and Edit User and Delete User
    Given I am logged into OrangeHRM
    And I navigate to Admin
    When I create a new user
    Then the user should be displayed in the user list
    And edit the user which is created
    Then delete the user which is created and verify it
    