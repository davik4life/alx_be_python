positiveInteger = int(input("Enter the size of the pattern: "))

row = 0

while row < positiveInteger:
    for i in range(positiveInteger):
        print("*", end="")
    print()
    row += 1
