user = list(input("Enter someting: "))
n = len(user)

for i in range(n // 2):
    user[i], user[n-1-i] = user[n-1-i], user[i]
print("Reversed String: ", "".join(user))