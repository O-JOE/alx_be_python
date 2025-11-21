# daily_reminder.py

# Prompt user for task
task = input("Enter your task: ")

# Prompt for priority level
priority = input("Priority (high/medium/low): ").lower()

# Prompt for time-bound status
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority using Match Case
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = "Invalid priority level entered."

# Modify reminder based on time-bound status
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print(reminder)