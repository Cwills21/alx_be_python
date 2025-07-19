# daily_reminder.py

# Step 1: Prompt user for task details
task = input("Enter your task: ").strip()

# Step 2: Get and validate priority
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ("high", "medium", "low"):
        break
    else:
        print("Invalid input. Please enter: high, medium, or low.")

# Step 3: Get and validate time-bound input
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ("yes", "no"):
        break
    else:
        print("Invalid input. Please enter: yes or no.")

# Step 4: Match priority and build base reminder
match priority:
    case "high":
        base_reminder = f"'{task}' is a high priority task"
    case "medium":
        base_reminder = f"'{task}' is a medium priority task"
    case "low":
        base_reminder = f"'{task}' is a low priority task"
    case _:
        # fallback (shouldn't occur due to validation)
        base_reminder = f"'{task}' is a task"

# Step 5: Append message based on time sensitivity
if time_bound == "yes":
    base_reminder += " that requires immediate attention today!"
else:
    base_reminder += ". Consider completing it when you have free time."

# Step 6: Print the final customized reminder
print("\n✅ Customized Reminder:")
print("Reminder:", base_reminder)
