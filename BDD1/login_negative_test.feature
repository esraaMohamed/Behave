Feature: Logging in with invalid credentials
  Scenario: Invalid user name
    Given I created a new user
    When I enter an invalid username
    And I entered a password
    And Clicked on the login button
    Then I should get an error message Invalid User

  Scenario: Invalid password
    Given I created a new user
    When I entered a valid username
    And I entered an invalid password
    And Clicked on the login button
    Then I should get an error message Invalid Password

  Scenario: User does not exist
    Given I have a random email address
    When I entered the random email address as the username
    And I entered a password
    And Clicked on the login button
    Then I should get an error message User does not exist

  Scenario: Login with no username and password
    Given I created a new user
    When I click on the login button
    Then I should get an error message saying that the username and password fields are mandatory

