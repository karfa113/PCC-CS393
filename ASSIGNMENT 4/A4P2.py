L = list(map(int, input("Enter numbers separated by space for the 1st list: ").split()))
M = list(map(int, input("Enter numbers separated by space for the 2nd list: ").split()))
N = []

if len(L) != len(M):
    print("Length of both list should be same ! ")
else:
    for i in range(len(L)):
        N.append(L[i] + M[i])

print(N)