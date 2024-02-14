Feature: Product Accessibility

  Scenario Outline: Access Products Categories
    Given I am a user of the website
    When I visit the news website
    And I click on the <category_name> category
    Then I should be taken to <category_name> category
    And the category should show at least <num_products> products
    When I click on the first product in the results
    Then I should be taken to the details page for that product
    Examples:
      | category_name    | num_products |
      | Signed           | 1            |
      | Bestsellers      | 3            |
      | Bookseller-picks | 2            |
      | Childrens        | 2            |
      | Poetry           | 2            |

  Scenario: Search and View Product Details
    Given I am a user of the website
    When I visit the news website
    When I search for a product using the term book
    Then I should see the search results
    And there should be at least 5 products in the search results
    When I click on the first product in the results
    Then I should be taken to the details page for that product

  Scenario: User login
    Given I am a user of the website
    When I visit the news website
    And I visit the login page
    And I enter the user email
    And I enter the user password
    Then User should be logged in

  Scenario: Add to Cart and then Remove
    Given I am a user of the website
    When I visit the news website
    When I go to the books section
    When I click on the first product in the results
    Then I should be taken to the details page for that product
    When I click on the add to cart button
    Then I go to the cart
    Then I should be taken to the cart page
    Then I remove product from the cart
