nums = sorted(map(int, input("Enter numbers seperated by space: ").split()))
mid = len(nums) // 2
if len(nums) % 2 != 0:
    print(f"Median - {nums[mid]}")
else:
    print(f"Median - {(nums[mid - 1] + nums[mid]) / 2}")
