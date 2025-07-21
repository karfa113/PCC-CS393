n = int(input("Enter the number of elements: "))

if n < 2:
    print("Please enter atleast 2 numbers")
else:
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)

numbers.sort()
print(numbers)

print(f"Second larget number is: {numbers[n-2]}")