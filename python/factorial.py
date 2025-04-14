n = int(input("Enter an integer: "))

factorial = 1

for i in range(1, n + 1): # 1, 2, 3, 4, 5
    factorial = factorial * i
print(f"The factorial of {n} is: {factorial}")