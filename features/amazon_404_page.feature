Feature: Tests for 484 page

  Scenario: User is able to navigate to amazon blog from 484 page
    Given Open Amazon product B07NF5WGQ11111111 page
    And Store original window
    When Click on a dog image
    And Switch to new window
    Then Verify blog is opened
    And Close blog
    And Return to original window

