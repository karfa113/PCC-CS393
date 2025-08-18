def circle(r):
    return 3.14 * r * r

def square(s):
    return s * s

def rectangle(l, b):
    return l * b

def triangle(base, height):
    return 0.5 * base * height

print("=== AREA CALCULATOR ===")
print("1. Circle")
print("2. Square")
print("3. Rectangle")
print("4. Triangle")
print("=======================")
choice = int(input("Enter your choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    print(f"Area of the circle: {circle(r)}")
elif choice == 2:
    s = float(input("Enter side length: "))
    print(f"Area of the square: {square(s)}")
elif choice == 3:
    l = float(input("Enter length: "))
    b = float(input("Enter bredth: "))
    print(f"Area of the rectangle: {rectangle(l, b)}")
elif choice == 4:
    base = float(input("Enter base length: "))
    height = float(input("Enter height: "))
    print(f"Area of the triangle: {triangle(base, height)}")
else:
    print("Invalid Choice")