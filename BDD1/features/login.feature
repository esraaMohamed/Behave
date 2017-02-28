Feature: Login to portal

  Scenario: Login and logout
    Given I open the website
    When I login with "mngr66332" and "vavYren"
    Then I should see a welcome message
