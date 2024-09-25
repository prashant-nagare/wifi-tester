import sys
import time
import threading

# Flag to control the spinner animation
stop_spinner = False

def spinner_animation():
    spinner = ['|', '/', '-', '\\']
    while not stop_spinner:
        for symbol in spinner:
            # Clear the last line and print the spinner
            sys.stdout.write(f'\r{symbol} Loading...       ')  # Add spaces to clear remaining chars
            sys.stdout.flush()
            time.sleep(0.2)
            if stop_spinner:
                break

def long_running_task():
    for i in range(10):
        # Move the cursor up, clear the old line, and print a new message
        sys.stdout.write(f'\rProcessing step {i+1}...          ')
        sys.stdout.flush()
        time.sleep(1)  # Simulate work

# Start the spinner in a separate thread
spinner_thread = threading.Thread(target=spinner_animation)
spinner_thread.start()

# Run the long-running task
long_running_task()

# Stop the spinner after the task is completed
stop_spinner = True
spinner_thread.join()  # Ensure spinner thread stops

# Clear the spinner line and print the final message
sys.stdout.write('\rTask completed!        \n')
