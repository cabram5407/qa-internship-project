# Created by cabram54 at 11/7/2024

Feature: reelly setting and profile UI

  Scenario: User can go to settings and edit the personal information
  Given Open the main page
  When Log in to the page
  And Click on settings option
  And Click on Edit profile option
  And Enter some test information in the input fields
  Then Check the right information is present in the input fields
  And Check “Close” and “Save Changes” buttons are available and clickable