import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def execute_task(task_name, task_function):
    """Execute a task safely and log the result."""
    try:
        logging.info(f"Starting task: {task_name}")
        result = task_function()
        logging.info(f"Task completed successfully: {task_name}")
        return result

    except Exception as error:
        logging.error(f"Task failed: {task_name} | Error: {error}")
        return None


# Example tasks
def backup_data():
    print("Creating data backup...")
    return "Backup completed"


def process_data():
    print("Processing data...")
    return "Data processed"


def faulty_task():
    print("Running a task that may fail...")
    raise ValueError("Example error during task execution")


# Execute tasks independently
tasks = [
    ("Data Backup", backup_data),
    ("Data Processing", process_data),
    ("Faulty Task", faulty_task),
    ("Final Backup", backup_data)
]

for task_name, task_function in tasks:
    execute_task(task_name, task_function)

print("All tasks have been processed.")
