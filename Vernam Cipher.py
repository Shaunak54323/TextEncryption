def matrixKey(key, length):
    keyMatrix = []
    for i in range(length // len(key)):
        for j in range(len(key)):
            keyMatrix.append(ord(key[j]) % 65)
    if length % len(key) != 0:
        for i in range(length % len(key)):
            keyMatrix.append(ord(key[i]) % 65)
    return keyMatrix
def matrixMessage(message):
    messageMatrix = []
    for i in range(len(message)):
        messageMatrix.append(ord(message[i]) % 65)
    return messageMatrix
def messageEncryprt(keyMatrix, messageMatrix):
    cipherMatrix = []
    for i in range(len(keyMatrix)):
        cipherMatrix.append((messageMatrix[i] + keyMatrix[i]) % 26)
    return cipherMatrix
def messageDecrypt(keyMatrix, messageMatrix):
    decryptMessageMatrix = []
    for i in range(len(keyMatrix)):
        decryptMessageMatrix.append((messageMatrix[i] - keyMatrix[i]) % 26)
    return decryptMessageMatrix
def displayMatrix(matrix):
    for i in range(len(matrix)):
        matrix[i] = (chr(matrix[i] + 65))
    return "".join(matrix)
choice = 0
while choice != 3:
    choice = int(input("[1] Encrption\n[2] Decryption\n[3] Exit\nEnter your choice:"))
    if choice == 1:
        print("*ENTER KEY LESS THAN OR EQUAL TO THE LENGTH OF MESSAGE")
        messageMatrix = matrixMessage(input("Enter message: ").upper())
        keyMatrix = matrixKey(input("Enter key:").upper(), len(messageMatrix))
        encryptMessage = messageEncryprt(keyMatrix, messageMatrix)
        print("Encrypted Message: ", displayMatrix(encryptMessage), "\n")
    elif choice == 2:
        print("*ENTER KEY LESS THAN OR EQUAL TO THE LENGTH OF ENCRYPTED MESSAGE")
        encryptedMessageMatrix = matrixMessage(input("Enter encrypted message: ").upper())
        keyMatrix = matrixKey(input("Enter key:").upper(), len(messageMatrix))
        decryptMessage = messageDecrypt(keyMatrix, encryptedMessageMatrix)
        print("Decrypted Message: ", displayMatrix(decryptMessage), "\n")
    elif choice == 3:
        print("Exiting...")
        exit(0)
    else:
        print("Invalid choice, try again!")