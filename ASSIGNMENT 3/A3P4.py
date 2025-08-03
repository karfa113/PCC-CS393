user = input("Enter a string: ").lower()
reverse = user[::-1]

print("Palindrome" if user == reverse else "Not Palindrome")