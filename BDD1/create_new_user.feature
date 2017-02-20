Feature: Creating a new user
  Scenario: User created successfully
    Given I generated a random email address
    When I enter the email in the username field
    And I enter the password in the password field
    And Click on the signup button
    Then I should see a welcome message