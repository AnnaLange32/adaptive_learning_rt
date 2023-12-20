import time

# Set the initial time
experiment_start_time = time.time()
emotion_timer = time.time()

# Define the interval (in seconds) for the task (5 minutes in this case)
interval = 5 * 60  # 5 minutes * 60 seconds/minute
experiment_end_time = 30 * 60 # 30 minutes * 60 seconds/minute

while experiment_start_time < experiment_end_time:


    # Check if it's time to perform the task
    if current_time - emotion_timer >= interval:
        # Perform your task here
        print("Performing the task!")

        # Update the start time for the next interval
        emotion_timer = current_time

    # You can add other code or sleep for a shorter time to reduce CPU usage
    # time.sleep(1)  # Sleep for 1 second, for example
