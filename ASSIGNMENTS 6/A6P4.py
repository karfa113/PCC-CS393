# Bubble sort

def bubble(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

lst = list(map(int, input("Enter numbers: ").split()))
print(bubble(lst))