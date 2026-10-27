Feature: OrangeHRM Leave

  Scenario: Apply for Leave
    Given I am logged into OrangeHRM
    And Navigate to Leave Page
    And Go to Apply Leave 
    When Add deatils of Apply Leave and Apply
    Then Verify the Leave from my leave tab
    And add comment to leave
    