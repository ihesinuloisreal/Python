year = int(input("Enter year: "))

test_1 = year % 4
test_2 = year % 100
test_3 = year % 400

if test_1 == 0:
    if test_2 == 0:
        if test_3 == 0:
            print("The Year is a leap Year!!!")
        else:
            print("The Year is not a leap Year!!!")
    else:
        print("The Year is a leap Year!!!")
else:
    print("The Year is not a leap Year!!!")