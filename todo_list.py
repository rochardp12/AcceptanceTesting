import json
import os

FILE_PATH = 'todo_list.json'

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({'description': description, 'status': 'Pending'})
    save_tasks(tasks)

def list_tasks():
    return load_tasks()

def mark_task_completed(description):
    tasks = load_tasks()
    for task in tasks:
        if task['description'] == description:
            task['status'] = 'Completed'
    save_tasks(tasks)

def clear_tasks():
    save_tasks([])

def print_tasks():
    tasks = list_tasks()
    if tasks:
        print("Tasks:")
        for task in tasks:
            print(f"- {task['description']} ({task['status']})")
    else:
        print("No tasks found.")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='To-Do List Manager')
    parser.add_argument('action', choices=['add', 'list', 'complete', 'clear'], help='Action to perform')
    parser.add_argument('description', nargs='?', help='Task description')

    args = parser.parse_args()

    if args.action == 'add' and args.description:
        add_task(args.description)
    elif args.action == 'list':
        print_tasks()
    elif args.action == 'complete' and args.description:
        mark_task_completed(args.description)
    elif args.action == 'clear':
        clear_tasks()
    else:
        print("Invalid arguments")