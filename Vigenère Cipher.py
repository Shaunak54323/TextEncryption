def generateKey(message, key):
    key = list(key)
    if len(message) == len(key):
        return (key)
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)
def cipherMessage(message, key):
    cipher_text = []
    for i in range(len(message)):
        x = (ord(message[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)
def originalMessage(cipherMessage, key):
    origMessage = []
    for i in range(len(cipherMessage)):
        x = (ord(cipherMessage[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        origMessage.append(chr(x))
    return "".join(origMessage)
choice = 0
while choice != 3:
    choice =int(input("[1] Encryption\n[2] Decryption\n[3] Exit\nEnter your choice:"))
    if choice == 1:
        message = input("Enter message:").upper()
        key = generateKey(message, input("Enter key: ").upper())
        print("Encrypted Message:", cipherMessage(message, key))
    elif choice == 2:
        encryptedMessage = input("Enter encrypted message:").upper()
        key = generateKey(encryptedMessage, input("Enter key: ").upper())
        print("Decrypted Message:", originalMessage(encryptedMessage, key))
    elif choice == 3:
        print("Exiting...")
        exit(0)
    else:
        print("Invalid choice, try again!")
