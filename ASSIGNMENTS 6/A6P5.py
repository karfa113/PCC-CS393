# Binary search

def search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

lst = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target element: "))
lst.sort()
print(f"Sorted: {lst}")
print(f"Element found at index: {search(lst, target)}" if search(lst, target) != -1 else "Element not found")