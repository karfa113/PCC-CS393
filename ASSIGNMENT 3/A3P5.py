def superascii(word):
    hm = {}
    for i in range(96, 123):
        hm[chr(i)] = i-96
    for ch in word:
        if not word.count(ch) == hm[ch]:
            return 0
    return 1

user = input("Enter the string: ").lower()
print("Super ASCII" if superascii(user) else "Not a Super ASCII")