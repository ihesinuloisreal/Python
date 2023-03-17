height = float(input("What is your height "))
weight = int(input("What is your weight "))

BMI = round(weight / height ** 2)

if BMI < 18.5:
    print("You are underweight")
elif BMI < 25:
    print("You are normal weight")
elif BMI < 30:
    print("You are overweight")
elif BMI < 35:
    print("You are Obese")
else:
    print("You are Clinically obese")


# print(int(BMI))