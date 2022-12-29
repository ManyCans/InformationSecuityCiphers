plntext= input("Enter Plain text here.. ").lower()
key=input("Enter Your key.. ")
for i in range(len(plntext)):
    k=(ord(plntext[i])-(ord('a')))+(ord(key[(i%(len(key)))])-(ord('a')))
    print(chr((k%26)+ord('a')),end="")
print("")
ctxt =input("Enter Your cipher text.. ")
keyy=input("Enter Your key.. ")
for i in range(len(ctxt)):
    k=(ord(ctxt[i])-ord('a'))-(ord(keyy[(i%(len(keyy)))])-ord('a'))
    print(chr((k%26) +ord('a')),end="")

    
