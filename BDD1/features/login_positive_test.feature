Feature: Logging in using a valid username and password
  Scenario: User login successfully
    Given I open the website
    When I enter the user name
    And I enter the password
    And Click on the login button
    Then I should see a welcome message



