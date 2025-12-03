#!/usr/bin/env python3
"""
explore_datetime.py - Demonstrates usage of the datetime module
"""

from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    """Calculate and print the future date after adding the given number of days."""
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    return future_date

def main():
    current_dt = display_current_datetime()

    while True:
        try:
            days_input = input("Enter the number of days to add to the current date: ").strip()
            days = int(days_input)
            if days < 0:
                print("Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
        except (EOFError, KeyboardInterrupt):
            print()  # clean newline on Ctrl+D/Ctrl+C
            return

    calculate_future_date(current_dt, days)

if __name__ == "__main__":
    main()