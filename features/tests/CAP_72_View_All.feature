# Created by Kevin at 12/14/22
Feature: View All link functionality

  Scenario: Click on the View All link, and see more products
    Given Open CureSkin page
    When Click on View All button
    Then Verify the Products header

