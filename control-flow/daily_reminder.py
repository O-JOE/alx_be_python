task = input("Enter the task you want to be reminded of: ")
priority = input("Enter the priority level (high, medium, low): ").lower()
time_bound = input("Is this a time-bound task? (yes/no): ").lower()
match priority:
    case "high":
        print(f"Reminder: You have a HIGH priority task - '{task}'. Please address it immediately!")
    case "medium":
        print(f"Reminder: You have a MEDIUM priority task - '{task}'. Try to complete it soon.")
    case "low":
        print(f"Reminder: You have a LOW priority task - '{task}'. You can attend to it at your convenience.")
    case _:
        print("Invalid priority level entered.")
if time_bound == "yes":
    print("{task} is a high priority task that requires immediate attention today!")
else:
    print(f"{task} is a low priority task. Consider completing it when you have free time.")
