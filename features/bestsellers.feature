Feature: Tests for bestseller functionality

#  Scenario: Bestsellers links can be opened
#    Given Open Amazon Bestsellers
#    Then Verify there are 5 links


 # HW 6

  Scenario: User can click on each Best Sellers links and verify that correct page opens
    Given Open Amazon Bestsellers
    When Click on BestSellers button
    Then Verify user sees "Amazon Best Sellers" text
    When Click on New Releases button
    Then Verify user sees "Amazon Hot New Releases" text
    When Click on Movers&Shakers button
    Then Verify user sees "Amazon Movers & Shakers" text
    When Click on Most Wished For button
    Then Verify user sees "Amazon Most Wished For" text
    When Click on Gift Ideas
    Then Verify user sees "Amazon Gift Ideas" text


