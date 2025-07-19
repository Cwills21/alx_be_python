# daily_reminder.py

# Prompt user for task input
task = input("Enter your task: ").strip()

# Validate priority input using a loop
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ("high", "medium", "low"):
        break
    else:
        print("Please enter a valid priority: high, medium, or low.")

# Validate time-bound input using a loop
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ("yes", "no"):
        break
    else:
        print("Please enter 'yes' or 'no'.")

# Use match-case to determine the response based on priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# Modify the reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Display the final reminder
print("\nReminder:", reminder)
