#Solution in Python

age = input("Tell me What is your current age?")
new_age = int(age)
remaining_years = 90 - new_age
days_remaining = remaining_years * 365 
weeks_remaining = remaining_years * 52
month_remaining = remaining_years * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {month_remaining} months left.")



