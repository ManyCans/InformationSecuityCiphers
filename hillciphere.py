from pydoc import plain


# n = input("enter the number of letters in your key,say n - ")
key = input("Enter your key - ")
plain_text=input("Enter your plain text - ")

key_matrix=[[0]*3 for i in range(3)]
k=0
for i in range(3):
    for j in range(3):
        key_matrix[i][j]= ord(key[k])-ord('a')
        k+=1
k=0
for i in range(3):
    for j in range(3):
        val=0
        for k in range(3):
            val = key_matrix[i] 
        print(val)
        k+=1
    print(" ")

