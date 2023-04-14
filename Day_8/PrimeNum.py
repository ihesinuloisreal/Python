def prime_checker(number):
    if number > 1 :
        for i in range(2, number) :
            if (number % i) == 0 :
                print(f"it's Not a prime number")
                break
            else :
                print(f"It's a prime number")
    else : 
        print("It's not a prime number")

prime_checker(number = 6)