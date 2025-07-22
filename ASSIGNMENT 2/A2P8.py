num = int(input("Enter a number: "))

while num > 9:
    sum = 0
    while num > 0:
        temp = num % 10
        sum += temp
        num = int(num/10)
    num = sum

if sum == 1:
    print("Magic number")
else:
    print("Not a Magic number")