import string

def superascii(word):
    freq = {}
    for ch in word:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
            
    # for key, value in freq.items():
    #     print(f"{key}: {value}")

    for ch in freq:
        if freq[ch] != (ord(ch) - 96):
            return False
    return True

user = input("Enter the string: ").lower()

if superascii(user):
    print("It is a Super ASCII")
else:
    print("It is not a Super ASCII")