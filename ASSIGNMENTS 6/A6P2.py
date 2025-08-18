def func(num):
    return [i for i in range(num, num + 10)]

lst = int(input("Enter starting number: "))
print(func(lst))