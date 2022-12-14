# Created by Kevin at 12/13/22
Feature: Reviews section functionality

  Scenario: Click on a product, then get redirected to reviews
    Given Open CureSkin page
    When Click on a product
    And Click on star/reviews near description
    Then Verify reviews section

