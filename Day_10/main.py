# def format_name(f_name, l_name):
#     fname = f_name.title()
#     lname = l_name.title()
#     return f"{fname} {lname}"
# formatted = format_name("israel", "hope")
# print(formatted)

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
                # print("The Year is a leap Year!!!")
            else:
                return False
                # print("The Year is not a leap Year!!!")
        else:
            return True
            # print("The Year is a leap Year!!!")
    else:
        return False
        # print("The Year is not a leap Year!!!")

def days_of_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) == True and month == 2:
        return 29
    return f"Year: {year}, Month: {month_days[month-1]}"

year = int(input("Enter year: "))
month = int(input("Enter month: "))
days = days_of_month(year,month)
print(days)

