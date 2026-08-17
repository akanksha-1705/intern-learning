import argparse
import json
from pathlib import Path


TASKS_FILE = Path(__file__).parent / "tasks.json"


def load_tasks():
    """Load tasks from tasks.json."""
    if not TASKS_FILE.exists():
        return []

    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    """Save tasks to tasks.json."""
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def add_task(task_text):
    """Add a new task."""
    tasks = load_tasks()

    tasks.append(task_text)
    save_tasks(tasks)

    print(f"Task added: {task_text}")


def list_tasks():
    """Display all tasks."""
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def remove_task(task_number):
    """Remove a task by its number."""
    tasks = load_tasks()

    if task_number < 1 or task_number > len(tasks):
        print(f"Invalid task number: {task_number}")
        print(f"Please choose a number between 1 and {len(tasks)}.")
        return

    removed_task = tasks.pop(task_number - 1)
    save_tasks(tasks)

    print(f"Task removed: {removed_task}")


def create_parser():
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="A simple command-line To-Do application."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    add_parser = subparsers.add_parser(
        "add",
        help="Add a new task."
    )

    add_parser.add_argument(
        "task",
        help="The task description."
    )

    subparsers.add_parser(
        "list",
        help="List all tasks."
    )

    remove_parser = subparsers.add_parser(
        "remove",
        help="Remove a task by number."
    )

    remove_parser.add_argument(
        "number",
        type=int,
        help="The task number to remove."
    )

    return parser


def main():
    """Run the command-line application."""
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "add":
        add_task(args.task)

    elif args.command == "list":
        list_tasks()

    elif args.command == "remove":
        remove_task(args.number)


if __name__ == "__main__":
    main()