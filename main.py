import sched
import time
import threading

def print_event(name):
    """Print the name of the scheduled event."""
    print(f"Event: {name} at {time.time()}")

def long_running_task(name, duration):
    """A long-running task that takes some time to complete."""
    print(f"Long Running Task: {name} started at {time.time()}")
    time.sleep(duration)
    print(f"Long Running Task: {name} finished at {time.time()}")

# Create a scheduler object
scheduler = sched.scheduler(time.time, time.sleep)

# Function to schedule a long-running task
def schedule_long_running_task(name, delay, duration):
    """Schedule a long-running task with threading."""
    scheduler.enter(delay, 1, threading.Thread(target=long_running_task, args=(name, duration,)).start)

# Schedule some events
scheduler.enter(5, 1, print_event, ('First Event',))
scheduler.enter(10, 1, print_event, ('Second Event',))
scheduler.enter(15, 1, print_event, ('Third Event',))

# Schedule long-running tasks
schedule_long_running_task('Task 1', 3, 5)
schedule_long_running_task('Task 2', 8, 7)

print(f"Scheduler started at {time.time()}")
scheduler.run()
print(f"Scheduler finished at {time.time()}")
