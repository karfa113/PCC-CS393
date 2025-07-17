items = int(input("Enter the number of items: "))

if items < 10 and items > 0:
    print(f"Total cost: {items * 120}rs")
elif items >= 10 and items <=99:
    print(f"Total cost: {items * 100}rs")
elif items >= 100:
    print(f"Total cost: {items * 70}rs")
else:
    print("Invalid input")