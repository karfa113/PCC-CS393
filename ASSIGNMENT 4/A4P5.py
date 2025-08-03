nums  = list(map(int, input("Enter numbers seperated by spaces: ").split()))
start, end = map(int, input("Enter starting and ending index: ").split())

if start > len(nums) or end > len(nums):
    print("Wrong index")
else:
    maxi = max(nums[start:end])
    mini = min(nums[start:end])

print(f"Maximum - {maxi}")
print(f"Minimum - {mini}")