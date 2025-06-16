# daily_reminder.py

# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match case to respond to priority
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to complete it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that still needs attention today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Plan to finish it this week.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task, but it's time-sensitive. Try not to delay it.")
        else:
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Reminder: Invalid priority entered. Please choose from high, medium, or low.")
