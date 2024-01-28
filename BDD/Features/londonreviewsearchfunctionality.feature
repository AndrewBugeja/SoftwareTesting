Feature: Products Search

  Scenario: Search and View Product Details
    Given I am a user of the website
    When I visit the news website
    When I search for a product using the term book
    Then I should see the search results
    And there should be at least 5 products in the search results
    When I click on the first product in the results
    Then I should be taken to the details page for that product