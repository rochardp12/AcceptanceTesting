# features/todo_list.feature

Feature: Manage tasks in the to-do list

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

    Scenario: Mark a task as completed
    Given the to-do list contains "Buy groceries"
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

    Scenario: Clear the entire to-do list
    Given the to-do list contains "Buy groceries"
    When the user clears the to-do list
    Then the to-do list should be empty
