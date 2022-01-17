def maximumOccuringLetter(str):
    allChar, max, letter = [0] * 256, -1, ""
    for i in str:
        allChar[ord(i)] += 1;
    for i in str:
        if max < allChar[ord(i)]:
            max = allChar[ord(i)]
            letter = i
    return letter
encryptedText = input("Enter Cipher Text: ").upper()
print("Max occurring character is '" + maximumOccuringLetter(encryptedText) + "' which will be matched to 'E'")
key = (ord("E") - ord(maximumOccuringLetter(encryptedText))) % 26
print("Hence, key =", key)
decryptedText = []
for i in encryptedText:
    decryptedText.append(chr((ord(i) - 65 + key) % 26 + 65))
print("Decrypted Text:", "".join(decryptedText))
