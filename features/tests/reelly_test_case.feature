# Created by cabram54 at 11/7/2024
Feature: UI setting and profile changes

  Scenario: User can edit the personal profile setting information
    Given Open the main page
    When Log in to the page
    And Click on settings option
    And Click on Edit profile option
    And Enter some test information in the input fields
    Then Check the right information is present in the input fields
    And Check “Close” and “Save Changes” buttons are available and clickable
