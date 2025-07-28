user = input("Enter a string: ")
user = list(user)

upper = 0
lower = 0
for i in user:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

print(f"Uppercase characters: {upper}")
print(f"Lowercase characters: {lower}")