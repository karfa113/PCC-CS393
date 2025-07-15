num = input("Enter a number: ")
temp = num[::-1]
print(f"Reversed number: {temp}")

if (int(num) % 2 == 0):
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")