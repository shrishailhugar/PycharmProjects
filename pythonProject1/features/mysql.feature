Feature: To add entry to mySQL
  @sql
  Scenario Outline: TO add entries to My SQL
    Given SQL <query>
    When user asks details of single user
    Then it should show customer details
    Examples:
    |query          |
    |getallcustomers|
