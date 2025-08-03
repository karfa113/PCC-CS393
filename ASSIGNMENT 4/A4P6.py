lst = list(map(int, input("Enter elements separated by space: ").split()))

seen = set()
unique = []
duplicates = []

for item in lst:
    if item not in seen:
        unique.append(item)
        seen.add(item)
    else:
        duplicates.append(item)

result = unique + duplicates
print("List after moving duplicates to the end:", result)
