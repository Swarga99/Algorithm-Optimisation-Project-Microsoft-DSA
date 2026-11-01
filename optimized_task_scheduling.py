import heapq


class TaskScheduler:
    def __init__(self):
        self.task_queue = []
        self.counter = 0

    def add_task(self, task_name, priority):
        # Negative priority makes a min-heap work as a max-priority queue
        heapq.heappush(
            self.task_queue,
            (-priority, self.counter, task_name)
        )
        self.counter += 1
        print(f"Task added: {task_name} (Priority: {priority})")

    def get_next_task(self):
        if not self.task_queue:
            return None

        priority, _, task_name = heapq.heappop(self.task_queue)
        return task_name, -priority

    def execute_tasks(self):
        while self.task_queue:
            task_name, priority = self.get_next_task()
            print(f"Executing: {task_name} (Priority: {priority})")


# Example usage
scheduler = TaskScheduler()

scheduler.add_task("Database Backup", 2)
scheduler.add_task("Process User Request", 5)
scheduler.add_task("Generate Report", 3)
scheduler.add_task("Security Check", 4)

scheduler.execute_tasks()
