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


#  Scenario: User sees correct amount of footer links
#    Given Open Amazon page
#    Then Verify there are 38 footer links

#
#  Scenario: User can sees correct amount of BestSellers links
#    Given Open Amazon BestSellers page
#    Then Verify there are 4 BestSellers links

# Test case #2

#  Scenario: User can add a product to the cart
#    Given Open Amazon page
#    When Search for Toys
#    And Click on the first product
#    And Click on Add to cart button
#    And Open cart page
#    Then Verify cart has 1 item(s)


  Scenario: User can sees Customer Service's UI elements
    Given Open Amazon Customer Service page
    Then Verify there are 9 Issue Card wrapper links
    Then Verify there are 11 Help Topics links