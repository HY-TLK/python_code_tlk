#-----------------------------------------------------------------------------
# Name:        Countdown timer  (004_countdown_timer.py)
# Purpose:    Write a program that starts at `10` and counts down to `1`,
#             but if the user enters `"stop"`, the countdown should break.
#
# Author:      Harry Yang
# Created:     04-Mar-2025
#-----------------------------------------------------------------------------

# Initialize the countdown starting number
count = 10

# Print the initial countdown number
print(count)

# Start a while loop that runs until count is greater than 1
while count > 1:
    # Ask the user for input to stop or continue
    user_input = input("Enter 'stop' to cancel or press Enter: ")

    # If the user enters "stop" (case-insensitive), break the loop
    if user_input.lower() == "stop":
        print("Stopping countdown...")
        break
    else:
        # Decrease the countdown number
        count -= 1
        # Print the updated countdown number
        print(count)
