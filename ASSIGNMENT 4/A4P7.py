num1 = list(map(int, input("Enter numbers separated by space for the 1st list: ").split()))
num2 = list(map(int, input("Enter numbers separated by space for the 2nd list: ").split()))

if len(num1) != len(num2):
    print("Error ! length is not same")
else:
    for i in range(0, len(num1)):
        if num1[i] != num2[i]:
            print(f"Differ at index - {i}")
            break