from pydoc import plain

n  =int(input("Enter the main number - "))
keyMatrix = [[0] * n for i in range(n)]
messageVector = [[0] for i in range(n)]
cipherMatrix = [[0] for i in range(n)]

def getKeyMatrix(key):
	k = 0
	for i in range(n):
		for j in range(n):
			keyMatrix[i][j] = ord(key[k]) -ord('a')
			k += 1

def encrypt(messageVector):
	for i in range(n):
		for j in range(1):
			cipherMatrix[i][j] = 0
			for x in range(n):
				cipherMatrix[i][j] += (keyMatrix[i][x]*messageVector[x][j])
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipher(message, key):
	getKeyMatrix(key)
	for i in range(n):
		messageVector[i][0] = ord(message[i]) -ord('a')
	encrypt(messageVector)
	CipherText = []
	for i in range(n):
		CipherText.append(chr(cipherMatrix[i][0] + ord('a')))
	print("Ciphertext: ", "".join(CipherText))


def main():
	message = input("Enter message of right length")
	msglist = []

	for i in range(int(len(message)/n)):
		k=[]
		for j in range(n):
			k.append(message[(n*i)+j])
		msglist.append(k)
		
	key = input("Enter the key of right length and fitting matrix")

	for i in range(int(len(message)/n)):
		HillCipher(msglist[i], key)

if __name__ == "__main__":
	main()
