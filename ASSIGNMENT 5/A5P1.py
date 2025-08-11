def unique(lst):
    lst = set(lst)
    return list(lst)

lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print(unique(lst))