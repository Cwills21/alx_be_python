Task = input("Enter your task: ")
Priority = input("Priority (high, medium, low): ")
Time_bound = input("Is it time-bound? (yes or no): ")

match Priority:
    case "high":
        if Time_bound == "yes":
            print("Reminder:", Task,
                  " is a high priority task that requires immediate attention today!")
        else:
            print("Reminder:", Task,
                  " is a high priority task but can be done later within the today!")
    case "medium":
        if Time_bound == "yes":
            print("Reminder:", Task,
                  " is a medium priority task that requires immediate attention today!")
        else:
            print("Reminder:", Task,
                  " is a medium priority task but can be done later within the today!")
    case "low":
        if Time_bound == "yes":
            print("Reminder:", Task,
                  " is a low priority task but requires immediate attention today!")
        else:
            print("Reminder:", Task,
                  " is a low priority task. Consider completing it when you have free time")
    case _:
        print("No task description")
