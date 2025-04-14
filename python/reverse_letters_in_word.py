n = input("Enter a string: \n")

index = len(n) - 1
reversed_string = ''

while index >= 0:
    reversed_string += n[index]
    index-=1

print(reversed_string)

