Feature: Send order to the production queue

  Scenario: Order is successfully sent to the queue
    Given the API is running
    And the order queue is empty
    When an order is sent to the API with valid data
    Then the response status should be 201
    And the order should be sent to the production queue
