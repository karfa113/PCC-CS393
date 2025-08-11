nums = list(map(int, input("Enter numbers seperated by space: ").split()))
sum = 0
for num in nums:
    if num > 0:
        sum += num

print("Sum of positive numbers: ", sum)