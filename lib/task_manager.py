import csv
import os

class TaskManager:

    FILE = "tasks.csv"

    def __init__(self):
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["id", "task", "status"])

    def add_task(self, task):
        tasks = self.load_tasks()
        task_id = len(tasks) + 1

        with open(self.FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([task_id, task, "pending"])

        print(f"Task '{task}' added successfully.")

    def complete_task(self, task_id):
        tasks = self.load_tasks()

        for task in tasks:
            if int(task["id"]) == task_id:
                task["status"] = "completed"

        self.save_tasks(tasks)
        print(f"Task {task_id} marked as completed.")

    def load_tasks(self):
        tasks = []

        with open(self.FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(row)

        return tasks

    def save_tasks(self, tasks):
        with open(self.FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "task", "status"])
            writer.writeheader()
            writer.writerows(tasks)