import math

def prime(n):
    if n <= 1:
        return 0
    for i in range(2, (int(n/2)+1)):
        if n % i == 0:
            return 0
    return 1

num = int(input("Enter a number: "))
num = math.sqrt(num)
if prime(num):
    print("Square root is a Prime Number")
else:
    print("Square root is NOT a Prime Number")