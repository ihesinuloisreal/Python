print("Welcome to our tip calculator app")
bill = float(input("What is the total Bill? $"))
percentage = int(input("What percentage tip would you like to give? %"))
persons = int(input("How many persons are to split the bill"))

total_bill_with_per = bill * ((percentage/100) + 1) 
perc = total_bill_with_per / persons


print(f"Each person will pay ${perc}")