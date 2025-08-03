num = list(map(int, input("Enter numbers separated by space for numerators: ").split()))
denum = list(map(int, input("Enter numbers separated by space for denominators: ").split()))

if len(num) != len(denum):
    print("Error ! length is not same")
else:
    fractions = [num[i] / denum[i] for i in range(0, len(num))]

max_frac = max(fractions)
min_frac = min(fractions)

max_index = fractions.index(max_frac)
min_index = fractions.index(min_frac)

print(f"Largest Fraction: {num[max_index]}/{denum[max_index]} = {max_frac}")
print(f"Smallest Fraction: {num[min_index]}/{denum[min_index]} = {min_frac}")