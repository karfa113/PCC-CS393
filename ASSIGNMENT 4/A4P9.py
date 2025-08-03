def search(i):
    for j in range(len(lst)):
        if lst[j] == i:
            print(f"Element found at index - {j}")
            break

lst = list(map(int, input("Enter numbers separated by space for the 1st list: ").split()))
item = int(input("Enter a number: "))
search(item)