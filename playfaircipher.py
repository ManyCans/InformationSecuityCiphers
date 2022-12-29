def diagraph(text):
    diaplace=[]
    itr=0
    for i in range(2,len(text),2):
        diaplace.append(text[itr:i])
        itr=i
    diaplace.append(text[itr:])
    return diaplace

def replawithx(text):
    k= len(text)
    if(k%2==0):
        for i in range(0,k,2):
            if(text[i]==text[i+1]):
                new_word= text[0,i+1]+str('x')+text[i+1:]
                new_word= replawithx(new_word)
                break
            else:
                new_word=text
    else:
        for i in range(0,k-1,2):
            if(text[i]==text[i+1]):
                new_word = text[0,i+1] + str('x') + text[i+1:]
                new_word= replawithx(new_word)#recusrion to get new word in association to different length 
                break
            else:
                new_word = text
    return new_word            
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']

def makingtable(text):
    keyletter=[]
    for i in text:
        if(i=='n'):
            i='m'
        if i not in keyletter:
            keyletter.append(i)
    compele=[]
    for i in keyletter:
        if(i=='n'):
            i='m'
        if i not in compele:
            compele.append(i)
    for i in alphabets:
        if i not in compele:
            compele.append(i)
    matrix=[]
    while compele != []:
        matrix.append(compele[:5])
        compele= compele[5:]
    print(matrix)
    return matrix

def search(mat,key):
    for i in range(5):
        for j in range(5):
            if (mat[i][j]==key):
                return i, j     

def same_col_elements(mat,ele1_x,ele1_y,ele2_x,ele2_y):
    char1= ''
    if(ele1_x==4):
        char1= mat[0][ele1_y]
    else:
        char1= mat[ele1_x+1][ele1_y]
    char2= ''
    if(ele2_x==4):
        char2= mat[0][ele2_y]
    else:
        char2= mat[ele2_x+1][ele2_y]
    return char1 ,char2

def same_row_elements(mat,ele1_x,ele1_y,ele2_x,ele2_y):
    char1= ''
    if(ele1_y==4):
        char1= mat[ele1_x][0]
    else:
        char1= mat[ele1_x][ele1_y+1]
    char2= ''
    if(ele2_y==4):
        char2= mat[ele2_x][0]
    else:
        char2= mat[ele2_x][ele2_y+1]
    return char1,char2

def switcheroo(matrix,ele1_x,ele1_y,ele2_x,ele2_y):
    char1= matrix[ele2_x][ele1_y]
    char2= matrix[ele1_x][ele2_y]
    return char1,char2

def encryptalgo(matrix,ptext):
    ciphertext=[]
    for i in range(len(ptext)):
        c1=''
        c2=''
        ele1_x,ele1_y=search(matrix,ptext[i][0])
        print(ele1_x,ele1_y)
        ele2_x,ele2_y=search(matrix,ptext[i][1])
        print(ele2_x,ele2_y)
        if ele1_x ==ele2_x:
            c1,c2= same_row_elements(matrix,ele1_x,ele1_y,ele2_x,ele2_y) 
        elif ele1_y ==ele2_y:
            c1,c2= same_col_elements(matrix,ele1_x,ele1_y,ele2_x,ele2_y) 
        else:
            c1,c2=switcheroo(matrix,ele1_x,ele1_y,ele2_x,ele2_y)
        cip = c2+c1
        ciphertext.append(cip)
    return ciphertext

def main():
    ptext = input("Enter the plain text here.. ")
    if(len(ptext)%2==1):
        ptext=ptext+"z"
    processedtext=diagraph(replawithx(ptext))
    key ="hero"
    matrix = makingtable(key)
    cipheredtext = encryptalgo(matrix,processedtext)
    print(cipheredtext)

if __name__=="__main__":
    main()