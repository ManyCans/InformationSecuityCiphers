#Solving Double Transposition 
def encrypt(ptext: str, key: str) -> str :
    matrix = []
    i = 0
    canExit = False
    for _ in ptext:
        if (canExit): break;
        row = []
        for _ in key:
            if (i >= len(ptext)): 
                row.append('X')
                canExit = True
            else:
                row.append(ptext[i])
                i += 1
        if (row != []) :
            matrix.append(row)
    print(matrix)
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

def decrypt(ptext: str, key:str) -> str:
    matrix = []
    i = 0
    for char in ptext:
        row = []
        for _ in range(len(ptext) // len(key)):
            if (i >= len(ptext)): 
                row.append('X')
                continue
            else:
                row.append(ptext[i])
                i += 1
        if (row != []):
            matrix.append(row)

    # print(matrix)

    ptext = ''
    for i in range(len(matrix[0])):
        for k in key:
            ptext += matrix[int(k) - 1][i]

    return ptext

if __name__ == "__main__":
    # mess age = input('Enter your message: ')
    # key = input('Enter your key: ')
    message = 'Hellothisisme'
    key ='4312567'
    key2 ='7652134'

    cipher = encrypt(message, key)
    print(cipher)

    cipher2 = encrypt(cipher, key2)
    print(cipher2)

    ptext = decrypt(cipher2, key2)
    pt = ''
    for i in range(len(cipher)):
        pt += ptext[i]
    print(pt)

    ptext2 = decrypt(pt, key)
    print(ptext2)
