def addx(text):
    num = len(text)
    if(num%2==0):
        for i in range(0,num,2):
            if(text[i]==text[i+1]):
                newword= text[0:i+1]+str('x')+text[i+1:]
                newword=addx(newword)
                break
            else:
                newword=text
    else:
        for i in range(0,num-1,2):
            if(text[i]==text[i+1]):
                newword=text[0:i+1]+str('x')+text[i+1:]
                newword=addx(newword)
                break
            else:
                newword=text   
    return newword
# add x to stop repeated words
## watch as our merge conflicts in master branch
#line 21 is commented

allchars =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
            's','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

def makeplyfarmtrx(key):
    tab=[]
    for i in (key):
        if i not in tab:
            tab.append(i)
    for i in allchars:
        if i not in tab:
            tab.append(i)
    return tab
# make a playfair mtrx list 

def exenit(word):
    if(len(word)%2==1):
        return (word+str('9'))
    else:
        return word
# evens our word lentgh

def divider(word):
    k=[]
    itr=0
    for i in range(2,len(word)+2,2):
        k.append(word[itr:i])
        itr=i
    return k
# list of 2 cahrsin listtaking input

def findplace(mmkmtx,chaar):
    for i in range(36):
        if(mmkmtx[i]==chaar):
            return i


def main():
    ptext=input("Enter plain Text . ")
    keytext = input('Enter key text ')
    keyl= (keytext)
    mkmtrx= makeplyfarmtrx(keyl)
    pl=divider(exenit(addx(ptext)))
    ourcipher=[]
    for i in pl:
        c1pos=findplace(mkmtrx,i[0])
        c2pos=findplace(mkmtrx,i[1])
        if((c1pos%6)==(c2pos%6)):
            c1pos=(c1pos+6)%36
            c2pos=(c2pos+6)%36
        elif((c1pos/6)==c2pos/6):
            if(c2pos%6==5):
                c2pos=c2pos-5
            else:
                c2pos+=1
            if(c1pos%6==5):
                c1pos=c1pos-5
            else:
                c1pos+=1
        else:
            x1=int(c1pos%6)
            y1=int(c1pos/6)
            x2=int(c2pos%6)
            y2=int(c2pos/6)
            c1pos=(y1*6)+x2
            c2pos=(y2*6)+x1
        ourcipher.append([mkmtrx[c1pos],mkmtrx[c2pos]])
    for i in ourcipher:
        for j in i:
            print(j,end='')
        print()

main()