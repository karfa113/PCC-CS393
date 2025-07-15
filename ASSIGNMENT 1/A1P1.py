n = int(input("Enter total number of years: "))
year = int(input("Enter the year: "))

print(f"In {n} years there are: ")
print(f"No. of days: {n * 365} days")
print(f"No. of hours: {n * 365 * 24} hours")
print(f"No. of minutes: {n * 365 * 24 * 60} minutes")
print(f"No. of seconds: {n * 365 * 24 * 60 * 60} seconds")

if (year % 4 == 0):
    if (year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print(f"{year} is not a leap year")