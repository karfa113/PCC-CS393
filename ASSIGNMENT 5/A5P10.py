def sum_positive(*args):
    return sum(x for x in args if x > 0)

numbers = map(int, input("Enter numbers separated by space: ").split())
print("Sum of positive numbers:", sum_positive(*numbers))