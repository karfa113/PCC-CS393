import math

data = list(map(float, input("Enter numbers separated by space: ").split()))

n = len(data)
mean = sum(data) / n
variance = sum((x - mean) ** 2 for x in data) / n
std_deviation = math.sqrt(variance)

print(f"Mean: {mean:.2f}")
print(f"Variance: {variance:.2f}")
print(f"Standard Deviation: {std_deviation:.2f}")