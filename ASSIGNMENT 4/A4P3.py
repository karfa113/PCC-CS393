str_list = list(input("Enter strings separated by space: ").split())
max_length = max(len(s) for s in str_list)

print(str_list)
print("Length of the longest string:", max_length)