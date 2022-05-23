Feature: Tests for bestseller functionality

  Scenario: Bestsellers links can be opened
    Given Open Amazon Bestsellers
    Then Verify there are 5 links