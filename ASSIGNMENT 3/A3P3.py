import string
pangram = True

user = list(input("Enter a sentence: ").lower())
letters = list(string.ascii_lowercase)

for i in letters:
    if i not in user:
        pangram = False
    
if pangram:
    print("It is a Pangram")
else:
    print("It is NOT a Pangram")