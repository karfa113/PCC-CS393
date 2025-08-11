def ispangram(s):
    c = set()
    for i in s:
        if i.isalpha() and i not in c:
            c.add(i)
    return len(c) == 26

user = list(input("Enter a sentence: ").lower())
print("Pangram" if ispangram(user) else "Not Pangram")