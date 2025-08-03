def encryption(s, key):
    enc = ""
    for ch in s:
        if ch.isalpha():
            enc += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        elif ch.isdigit():
            enc += str((int(ch) + key) % 10)
        else:
            enc += ch
    print(f"Input - {''.join(s)}")
    print(f"Encrypted message - {enc}")

def decryption(s, key):
    dec = ""
    for ch in s:
        if ch.isalpha():
            dec += chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
        elif ch.isdigit():
            dec += str((int(ch) - key) % 10)
        else:
            dec += ch
    print(f"Input - {''.join(s)}")
    print(f"Decrypted message - {dec}")

while True:
    choice = input("\nEnter E to encode, D to decode (q to quit): ").lower()
    if choice == "q":
        print("Thank you!")
        break
    text = input("Enter the text: ").lower()
    try:
        key = int(input("Enter the key (1–25): "))
    except ValueError:
        print("Invalid key, must be a number.")
        continue

    if not (0 < key < 26):
        print("Invalid key: must be between 1 and 25.")
        continue

    if choice == "e":
        encryption(text, key)
    elif choice == "d":
        decryption(text, key)
    else:
        print("Invalid choice.")
