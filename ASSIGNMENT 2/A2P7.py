rows = int(input("Enter number of rows: "))

for i in range(1, rows+1):
    spaces = rows - i
    print(" "*spaces, end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

for i in range(rows-1, 0, -1):
    spaces = rows - i
    print(" "*spaces, end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()