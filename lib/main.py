import argparse
from task_manager import TaskManager
import requests


def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    if response.status_code == 200:
        return response.json()

    return {}


def main():

    parser = argparse.ArgumentParser(description="Task CLI Tool")

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add-task")
    add_parser.add_argument("task", help="Task description")

    complete_parser = subparsers.add_parser("complete-task")
    complete_parser.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args()

    manager = TaskManager()

    if args.command == "add-task":
        manager.add_task(args.task)

    elif args.command == "complete-task":
        manager.complete_task(args.id)

    else:
        parser.print_help()


if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))

    main()