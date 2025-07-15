marks = int(input("Enter your marks: "))

if marks >= 100:
    print("Invalid input")
elif marks >= 91:
    print("Grade: O")
elif marks >= 81:
    print("Grade: A+")
elif marks >= 71:
    print("Grade: A")
elif marks >= 61:
    print("Grade: B")
elif marks >= 51:
    print("Grade: C")
elif marks >= 41:
    print("Grade: D")
elif marks >= 33:
    print("Grade: E")
elif marks >= 0:
    print("You Fail")
else:
    print("Invalid input")