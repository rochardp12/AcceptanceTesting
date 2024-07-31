# features/steps/todo_list_steps.py

from behave import given, when, then
from todo_list import add_task, list_tasks, mark_task_completed, clear_tasks, save_tasks, print_tasks
import os
import json

FILE_PATH = 'todo_list.json'

def reset_tasks(tasks):
    save_tasks(tasks)

@given('the to-do list is empty')
def step_given_empty_list(context):
    reset_tasks([])

@given('the to-do list contains "{description}"')
def step_given_tasks(context,description):
    add_task(description)

@when('the user adds a task "{description}"')
def step_when_add_task(context, description):
    add_task(description)

@when('the user lists all tasks')
def step_when_list_tasks(context):
    context.result = list_tasks()

@when('the user marks task "{description}" as completed')
def step_when_mark_task_completed(context, description):
    mark_task_completed(description)

@when('the user clears the to-do list')
def step_when_clear_tasks(context):
    clear_tasks()

@then('the to-do list should contain "{description}"')
def step_then_task_should_exist(context, description):
    tasks = list_tasks()
    assert any(task['description'] == description for task in tasks)

@then('the output should contain:')
def step_then_output_contains(context):
    expected_output = context.text.strip()
    tasks = list_tasks()
    actual_output = "Tasks:\n" + "\n".join(f"- {task['description']} ({task['status']})" for task in tasks)
    assert expected_output in actual_output


@then('the to-do list should show task "{description}" as completed')
def step_then_task_should_be_completed(context, description):
    tasks = list_tasks()
    task = next((task for task in tasks if task['description'] == description), None)
    assert task and task['status'] == 'Completed'

@then('the to-do list should be empty')
def step_then_list_should_be_empty(context):
    tasks = list_tasks()
    assert not tasks