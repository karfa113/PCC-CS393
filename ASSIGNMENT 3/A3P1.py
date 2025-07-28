word = input("Enter a string without any space: ")
word = list(word.lower())
i = 0

while i < len(word) - 1:
    if word[i] == word[i+1]:
        del word[i:i+2]
        i = 0
    else:
        i += 1

if word:
    for i in word:
        print(i, end="")
else:
    print("Empty String")
