plain_no=int( input("Enter your no - "))
p =int(input("Enter your large prime no - "))
q =int(input("Enter your 2nd large prime no - "))
n=p*q
tn=(p-1)*(q-1)
for i in range(tn-2):
    if(tn%(i+2)!=0):
        e=i+2
        break

for i in range(tn-1):
    d=0
    if((1+(i+1)*tn)%e==0):
        d=(1+(i+1)*tn)/e
        break
    if(d!=0):
        break

print("public key generated is (" + str(e) + ","+ str(n) +")") 
# print("private key generated is (" + str(d) + ","+ str(n) +")") 

pbkey = input()



ciphereno=1
for _ in range(e):
    ciphereno*=plain_no
ciphereno=ciphereno%n
print("This no is ciphere to "+str(ciphereno))

retrieved_message=1
for _ in range(int(d)):
    retrieved_message*=ciphereno
    if(retrieved_message>2000):
        retrieved_message=retrieved_message%n
retrieved_message=(retrieved_message)%n
print("This no is retrieved is "+str(retrieved_message))
