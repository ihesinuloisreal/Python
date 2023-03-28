import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','*','(',')','+']

print("Welcome to the PyPassword Generato!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

total = nr_letters + nr_numbers + nr_symbols

lett = []
nums = []
symb = []

for lt in range(1, nr_letters + 1):
    res=(random.randint(0, lt))
    lett.append(letters[res])

for num in range(1, nr_numbers + 1):
    res=(random.randint(0, num))
    nums.append(numbers[res])

for sym in range(1, nr_symbols + 1):
    res=(random.randint(0, sym))
    symb.append(symbols[res])

Gen_Pass =''.join(random.sample(lett + nums + symb, total)) 

print(Gen_Pass)



















# def shurfle(arr):
#     p = 0
#     b = 0
#     for i in range(len(arr)):
#         if b == 1:
#             b -= 1
#         elif arr[i] < 0:
#             arr[i], arr[p] = arr[p], arr[i]
#             if p > i:
#                 b += 1
#             p += 2
#     return arr
