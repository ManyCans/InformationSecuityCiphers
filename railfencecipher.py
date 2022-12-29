def d_encrypt(plainText: str) -> str:
    cipher = ''
    matrix = [['_' for i in range(len(plainText))]
                  for j in range(2)]
    i = 0
    altIndex = 0
    for char in plainText:
        matrix[altIndex][i] = char
        i += 1
        if (altIndex):
            altIndex = 0
        else:
            altIndex = 1
    
    # print(matrix)
    for row in matrix:
        for char in row:
            if(char == '_'): continue
            cipher += char

    return cipher

def d_decrypt(cipher: str) -> str:
    matrix = []
    tmpString = []

    alternateFlg = True
    i = 0
    count = 0
    while (i < len(cipher)):

        if (count == len(cipher)):
            matrix.append(tmpString)
            tmpString = []
            alternateFlg = False

        if (alternateFlg):
            tmpString.append(cipher[i])
            i += 1
        else :
            tmpString.append('_')

        alternateFlg = not alternateFlg
        count += 1

    matrix.append(tmpString)
    
    # print(matrix)

    plainText = ''
    index = 0
    altIndex = 0
    for _ in range(len(cipher)):
        plainText += matrix[altIndex][index]

        if (altIndex):
            altIndex = 0
        else:
            altIndex = 1
        
        index += 1

    return plainText

def encrypt(plainText: str, key: str) -> str :
    matrix = []
    i = 0
    canExit = False
    for _ in plainText:
        if (canExit): break;
        row = []
        for _ in key:
            if (i >= len(plainText)): 
                row.append('x')
                canExit = True
            else:
                row.append(plainText[i])
                i += 1
        if (row != []) :
            matrix.append(row)

    # print(matrix)

    kpt = {}
    i = 0
    for k in key:
        kpt[int(k)] = [row[i] for row in matrix]
        i += 1

    cipher = ''
    for i in range(len(kpt)):
        for j in range(len(kpt[i+1])):
            cipher += kpt[i+1][j]

    return cipher

def decrypt(plainText: str, key:str) -> str:
    matrix = []
    i = 0
    for char in plainText:
        row = []
        for _ in range(len(plainText) // len(key)):
            if (i >= len(plainText)): 
                continue
            else:
                row.append(plainText[i])
                i += 1
        if (row != []):
            matrix.append(row)

    # print(matrix)

    plainText = ''
    for i in range(len(matrix[0])):
        for k in key:
            plainText += matrix[int(k) - 1][i]

    return plainText

if __name__ == "__main__":
    message = input('Enter your message: ')
    key = input('Enter your key: ')
    # message = 'Datastructures'
    # key ='123'
    print('Old Method')
    cipher = d_encrypt(message)
    print(cipher)
    plainText = d_decrypt(cipher)
    print(plainText)
    print('\nNew Method')
    cipher = encrypt(message, key)
    print(cipher)
    plainText = decrypt(cipher, key)
    print(plainText)

