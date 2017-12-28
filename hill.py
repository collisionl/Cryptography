# coding = utf-8
import numpy as np

def Encryption():
	plainText = input('input plainText\n')
	plainText = plainText.lower()
	key = input('input cipher Matrix:')
	key = eval(key)							# 识别输入矩阵转为二维list
	lenOfGroup = len(key[0])				# 输入n*n的矩阵 既密文分组长度同样为n
	keymat = np.mat(key)					# list转为numpy中的矩阵

	plainTextList = list(plainText)
	for i in range(len(plainTextList)):		# 输入的密文转为list后逐个转为int
		plainTextList[i] = ord(plainTextList[i]) - 97

	while len(plainTextList) % lenOfGroup != 0:		# 不足一个分组的补0
		plainTextList.append(0)
	# 将密文list分为几个长度为密文分组长度的list并放入新list plainGroup是二维list
	plainGroup = [plainTextList[i:i+lenOfGroup] for i in range(0, len(plainTextList), lenOfGroup)]

	result = []								# 每个分组与密钥矩阵相乘，转为list，因为是二维的，所有取[0],append到新的list里
	for i in range(len(plainGroup)):
		result.append((np.mat(plainGroup[i]) * keymat).tolist()[0])

	cipherText = ''							# 将result中每个元素转位char，再全部拼接到cipher字符串
	for i in range(len(result)):
		for j in range(len(result[i])):
			result[i][j] = chr(result[i][j] % 26 + 97)
		cipherText += ''.join(result[i])
	print ('cipherText is:',cipherText.upper())




def Decryption():
	# cipherText = input('input cipherText\n')
	# cipherText = cipherText.lower()
	key = input('input cipher Matrix:')
	key = eval(key)
	lenOfGroup = len(key[0])
	keymat = np.mat(key)
	# 求转置矩阵？？？
	keymat = np.linalg.inv(keymat)
	print (keymat)
	# for i in range(len(keymat3[0])):
	# 	for j in range(len(keymat3[i])):
	# 		keymat3[i][j] = round(keymat3[i][j]) % 26
	# print (keymat3)
	

# if __name__ == '__main__':
# 	a = int(input('Encryption type 1, Decryption type 2\n'))
# 	if a == 1:
# 		Encryption()
# 	else:
# 		Decryption()

if __name__ == '__main__':
	# Encryption()
	Decryption()


# [[10,5,12,0,0],[3,14,21,0,0],[8,9,11,0,0],[0,0,0,11,8],[0,0,0,3,7]]
# http://blog.topspeedsnail.com/archives/1469