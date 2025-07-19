number = int(input("Enter a number to see its multiplication table:"))
multiplier = range(1, 11)
for factor in multiplier:
    print(number, " * ", factor, " = ", number*factor)
