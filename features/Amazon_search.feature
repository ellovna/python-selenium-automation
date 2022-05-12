# Created by Home PC at 4/28/2022
Feature: Tests for Amazon search

#
#  Scenario: Verify that user can search for products
#    Given Open Amazon page
#    When Search for coffee
#    Then Verify search results for "coffee" are shown

#
#  Scenario Outline: Verify that user can search for products
#    Given Open Amazon page
#    When Search for <search_word>
#    Then Verify search results for <search_result> is shown
#    Examples:
#    |search_word  |search_result  |
#    |coffee       |"coffee"       |


#
#
#Feature: Tests for Search on Amazon
#
#
#  Scenario: User can add a product to the cart
#    Given Open Amazon page
#    When Search for Spoons
#    And Click on the first product
#    And Click on Add to cart button
#    And Open cart page
#    Then Verify cart has 1 item(s)


#
#  Scenario: User sees ham menu btn on the main page
#    Given Open Amazon page
#    Then Verify hamburger menu btn present


  Scenario: User sees correct amount of footer links
    Given Open Amazon page
    Then Verify there are 38 footer links
