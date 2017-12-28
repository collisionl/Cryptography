# coding = utf-8
def Encryption():
	keyA = int(input('input keyA\n'))
	keyB = int(input('input keyB\n'))
	plainText = input('input plainText\n')
	plainText = plainText.lower()		# 如果明文输入为大写转为小写字母
	cipherText = ''						# 创建空cipher字符串
	for plainItem in plainText:
		# 先转为int 减掉 'a' 的ascii码后，进行加密运算， 结束后加'a' 的ascii码
		cipherText += chr(((ord(plainItem) - 97) * keyA + keyB ) % 26 + 97)
	print('cipher is:', cipherText.upper())

def Decryption():
	# keyA对应的逆元存入字典
	dit = {1:1, 3:9, 5:21, 7:15, 9:3, 11:19, 15:7, 17:23, 19:11, 21:5, 23:17, 25:25}
	keyA = int(input('input keyA\n'))
	keyB = int(input('input keyB\n'))
	cipherText = input('input cipherText\n')
	cipherText = cipherText.lower()		# 转为小写字母
	keyA = dit[keyA]					# 按照字典的索引查找对应逆元
	plainText = ''
	for cipherItem in cipherText:
		plainText += chr((keyA * (ord(cipherItem) - 97 - keyB)) % 26 + 97)
	print('plain is:', plainText)

def bruteForce():
	list1 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]		# keyA的所有取值
	list2 = [i for i in range(0,26)]						# keyB的所有取值
	cipherText = input('input cipherText\n')
	cipherText = cipherText.lower()
	# 循环尝试所有密钥组合 共312种 并输出
	a = 0
	for keyA in list1:					# 遍历keyA
		for keyB in list2:				# 遍历keyB
			a += 1
			plainText = ''				# plainText重置为空
			for cipherItem in cipherText:		# 对应单个明文破解
				plainText += chr((keyA * (ord(cipherItem) - 97 - keyB)) % 26 + 97)
			print('keyA =', keyA, 'keyB =', keyB, 'plain', a, 'is:', plainText)

if __name__ == '__main__':
	a = int(input('Encryption type 1, Decryption type 2, BruteForce type 3\n'))
	if a == 1:
		Encryption()
	elif a == 2:
		Decryption()
	else:
		bruteForce()
