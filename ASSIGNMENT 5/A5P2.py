import itertools

lst = input("Enter a list of numbers separated by spaces: ").split()
num = int(input("Enter the lengt of permutation/combination: "))
print("\nPermutations")
for p in itertools.permutations(lst, num):
    print(p)
print("\nCombinations")
for c in itertools.combinations(lst, num):
    print(c)