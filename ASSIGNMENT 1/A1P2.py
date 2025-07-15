p = float(input("Enter primary amount: "))
r = float(input("Enter rate of interest: "))
t = int(input("Enter time period (in years): "))

simple_interest = (p * t * r) / 100
simple_total = simple_interest + p
compound_interest =  p * ((1 + r / 100) ** t- 1)
compound_total = compound_interest + p

print(f"Simple interest: {simple_interest} rs")
print(f"Total amount (simple interest): {simple_total} rs")
print(f"Compound interest: {compound_interest:.2f} rs")
print(f"Total amount (compound interest): {compound_total:.2f} rs")