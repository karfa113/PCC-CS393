user = input("Enter a string: ").lower()
reverse = user[::-1]

if user == reverse:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")