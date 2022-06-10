Feature: Test for Click on Amazon Cart Icon


  Scenario: Verify that user can see "Amazon cart is empty" text
    Given Open Amazon page
    When Click on Cart Icon
    Then Verify 'Your Amazon Cart is empty' text present




