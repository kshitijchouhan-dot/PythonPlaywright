Feature: OrangeHRM Recruitment

  Scenario: Recruit Candidate 
    Given I am logged into OrangeHRM
    And Navigate to Recruitment Page
    When Add Candidates details 
    And Shortlist the candidate 
    Then Verify the candidate and status
    And Schedule the Interview of candidate and verify
    And Marked the candidate passed and verify
    