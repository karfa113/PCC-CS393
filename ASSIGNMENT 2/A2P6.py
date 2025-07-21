r = int(input("Enter number of rows: "))

for i in range(r, 0, -1):
    spaces = r - i
    print(" "*spaces, end="")
    star = (2 * i) -1
    print("*"*star, end="")
    print()