plntext =input("Enter your plain text... ")
key = int(input("Enter your key. "))
ctext=[]
for i in plntext:
    ctext.append(chr(((ord(i)+key-ord('a'))%26)+ord('a')))

for i in ctext:
    print(i,end="")
print("")

c2text =input("Enter your cipher text... ")
key2 = int(input("Enter your key. "))

for i in c2text:
    print(chr(((ord(i)-key-ord('a'))%26)+ord('a')),end="")