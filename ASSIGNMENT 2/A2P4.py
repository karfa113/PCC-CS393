numbers = []

while True:
    num = input("Enter a number (q to quit): ")
    if num.lower() == "q":
        break
    else:
        numbers.append(num)

for i in numbers:
    if i[::-1] == i:
        print(f"{i} is a Palindrome")