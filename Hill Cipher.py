import math
import numpy as np
from numpy.linalg import *


def getKeyMatrix(key, n):
    keyMatrix, k, key = [[0] * n for i in range(n)], 0, key.upper()
    for i in range(n):
        for j in range(n):
            keyMatrix[i][j], k = ord(key[k]) % 65, k + 1
    return keyMatrix


def getMessageMatrix(message, n):
    if len(message) % n != 0:
        message += ("0" * (n - (len(message) % n)))
    k, matrix = 0, [[0] * n for i in range(len(message) // n)]
    for i in range(len(message) // n):
        for j in range(n):
            matrix[i][j], k = ord(message[k]) % 65, k + 1
    return matrix


def multiplyMatrix(keyMatrix, messageMatrix, lengthMessageMatrix, n):
    cipherMatrix = [[0] * n for i in range(lengthMessageMatrix)]
    for i in range(lengthMessageMatrix):
        for j in range(n):
            cipherMatrix[i][j] = 0
            for x in range(n):
                cipherMatrix[i][j] += keyMatrix[j][x] * messageMatrix[i][x]
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26
    return cipherMatrix


def displayMatrix(cipherMatrix, lengthMessageMatrix, n):
    matrix = []
    for i in range(lengthMessageMatrix):
        for j in range(n):
            matrix.append(chr(cipherMatrix[i][j] + 65))
    print("".join(matrix))


def getDeterminantInverse(matrix, n):
    i = 0
    while (int(det(matrix).round()) % 26 * i) % 26 != 1:
        i += 1
    return i


def getMatrixInverse(matrix, n, d):
    arr = np.array(matrix)
    newMatrix = [[0] * int(math.sqrt(len(key)))
                 for i in range(int(math.sqrt(len(key))))]
    for i in range(n):
        for j in range(n):
            newMatrix[i][j] = (
                (int((inv(arr) * det(matrix))[i][j].round()) % 26) * d) % 26
    return newMatrix


choice = 0
while choice != 3:
    choice = int(
        input("[1] Encryption\n[2] Decryption\n[3] Exit\nEnter your Choice:"))
    if choice == 1:
        key = input("Enter Key: ").upper()
        keyMatrix = getKeyMatrix(key, int(math.sqrt(len(key))))
        message = input("Enter message: ").upper().replace(" ", "")
        if len(message) % int(math.sqrt(len(key))) != 0:
            message += ("0" * (int(math.sqrt(len(key))) -
                        (len(message) % int(math.sqrt(len(key))))))
        messageMatrix = getMessageMatrix(message, int(math.sqrt(len(key))))
        cipherMatrix = multiplyMatrix(keyMatrix, messageMatrix, len(message) // int(math.sqrt(len(key))),
                                      int(math.sqrt(len(key))))
        displayMatrix(cipherMatrix, len(message) //
                      int(math.sqrt(len(key))), int(math.sqrt(len(key))))
        print()
    elif choice == 2:
        key = input("Enter Key: ").upper()
        keyMatrix = getKeyMatrix(key, int(math.sqrt(len(key))))
        d = getDeterminantInverse(keyMatrix, int(math.sqrt(len(key))))
        keyInverse = getMatrixInverse(keyMatrix, int(math.sqrt(len(key))), d)
        message = input("Enter encrypted message: ").upper()
        temp = message
        if len(message) % int(math.sqrt(len(key))) != 0:
            message += ("0" * (int(math.sqrt(len(key))) -
                        (len(message) % int(math.sqrt(len(key))))))
        messageMatrix = getMessageMatrix(message, int(math.sqrt(len(key))))
        cipherMatrix = multiplyMatrix(keyInverse, messageMatrix, len(
            message) // int(math.sqrt(len(key))), int(math.sqrt(len(key))))
        displayMatrix(cipherMatrix, len(message) //
                      int(math.sqrt(len(key))), int(math.sqrt(len(key))))
        print()
    elif choice == 3:
        print("Exiting...")
        exit(0)
    else:
        print("Invalid Choice, try again:")
