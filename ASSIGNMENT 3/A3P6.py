import string

def encryption(user, int):
    letters = list(string.ascii_lowercase)
    output = []

    for ch in user:
        if ch in letters:
            index = letters.index(ch)
            new_index = (index + key) % 26
            output.append(letters[new_index])

        elif ch.isdigit():
            digit = int(ch)
            new_digit = (digit + key) % 10
            output.append(str(new_digit))

        else:
            output.append(ch)

    print("The output is: ")   
    for ch in output:
        print(ch,end="")

def decryption(user, int):
    letters = list(string.ascii_lowercase)
    output = []

    for ch in user:
        if ch in letters:
            index = letters.index(ch)
            new_index = (index - key) % 26
            output.append(letters[new_index])

        elif ch.isdigit():
            digit = int(ch)
            new_digit = (digit - key) % 10
            output.append(str(new_digit))

        else:
            output.append(ch)

    print("The output is: ")   
    for ch in output:
        print(ch,end="")
    
while True:
    choice = input("\nEnter E to encode, D to decode (q to quit): ").lower()
    if choice == "q":
        print("Thank You !")
        break
    text = input("Enter the text: ").lower()
    key = int(input("Enter the key: "))

    if choice == "e":
        encryption(text, key)
    elif choice == "d":
        decryption(text, key)
    else:
        print("Invalid Choice")
        continue     