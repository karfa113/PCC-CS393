def func(lst):
    maxi = max(lst)
    mini = min(lst)
    max_index = lst.index(maxi)
    min_index = lst.index(mini)
    return maxi, mini, max_index, min_index

lst = list(map(int, input("Enter numbers: ").split()))
a, b, c, d = func(lst)
print("Maximum element: ", a)
print("Index: ", c)
print("Minimum element: ", b)
print("Index: ", d)