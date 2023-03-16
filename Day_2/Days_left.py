age = int(input("What is your current age "))
age_left = 90 - age
num_days = age_left * 365
num_weeks = age_left * 52
num_months = age_left * 12

message = f"You have {num_days} days, {num_weeks} weeks and {num_months} months left"
print(message)