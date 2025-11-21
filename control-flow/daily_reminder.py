# daily_reminder.py

# Prompt user for task
task = input("Enter the task you want to be reminded of: ")

# Prompt for priority level
priority = input("Enter the priority level (high, medium, low): ").lower()

# Prompt for time-bound status
time_bound = input("Is this a time-bound task? (yes/no): ").lower()

# Process task based on priority using Match Case
match priority:
    case "high":
        reminder = f"Reminder: You have a HIGH priority task - '{task}'. Please address it immediately!"
    case "medium":
        reminder = f"Reminder: You have a MEDIUM priority task - '{task}'. Try to complete it soon."
    case "low":
        reminder = f"Reminder: You have a LOW priority task - '{task}'. You can attend to it at your convenience."
    case _:
        reminder = "Invalid priority level entered."

# Modify reminder based on time-bound status
if time_bound == "yes":
    reminder = f"'{task}' is a high priority task that requires immediate attention today!"
else:
    reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."

# Print the customized reminder
print(reminder)