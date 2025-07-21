def facto(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i

    return fact

def factoR(n):
    if n == 1:
        return 1
    
    return n * factoR(n-1)

num = int(input("Enter a number: "))
print(f"Factorial using recursion: {factoR(num)}")
print(f"Factorial without using recursion: {facto(num)}")