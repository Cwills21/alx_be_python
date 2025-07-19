task = input("Enter your task: ")
priority = input("Priority (high, medium, low): ")
time_bound = input("Is it time-bound? (yes or no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder:", task,
                  " is a high priority task that requires immediate attention today!")
        else:
            print("Reminder:", task,
                  " is a high priority task but can be done later within the today!")
    case "medium":
        if time_bound == "yes":
            print("Reminder:", task,
                  " is a medium priority task that requires immediate attention today!")
        else:
            print("Reminder:", task,
                  " is a medium priority task but can be done later within the today!")
    case "low":
        if time_bound == "yes":
            print("Reminder:", task,
                  " is a low priority task but requires immediate attention today!")
        else:
            print("Reminder:", task,
                  " is a low priority task. Consider completing it when you have free time")
    case _:
        print("No task description")
