# coding:utf-8
def initExchange(data):
	data = list(bin(data))[2:]		# 转为list
	data = ''.join(data)
	while len(data) < 64:
		data = '0' + data
	data = list(data)
	result = [0] * 64
	# 初始置换盒
	ip = [
	58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
	62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
	57, 49, 41, 33, 25, 17,  9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
	61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
	# 循环置换
	for i in range(64):
		result[i] = data[ip[i] - 1]
	return result

# S盒置换
def sBox(temp):
	# S盒
	s = [0] * 9
	s[1] = [
	[ 14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7 ],
	[ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8 ],
	[ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0 ],
	[ 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]]
	s[2] = [
	[ 15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10 ],
	[ 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5 ],
	[ 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15 ],
	[ 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]]
	s[3] = [
	[ 10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8 ],
	[ 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1 ],
	[ 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7 ],
	[ 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]]
	s[4] = [
	[ 7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15 ],
	[ 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9 ],
	[ 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4 ],
	[ 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14 ]]
	s[5] = [
	[ 2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9 ],
	[ 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6 ],
	[ 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14 ],
	[ 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]]
	s[6] = [ 
	[ 12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11 ],
	[ 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8 ],
	[ 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6 ],
	[ 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13 ]]
	s[7] = [
	[ 4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1 ],
	[ 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6 ],
	[ 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2 ],
	[ 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12 ]]
	s[8] = [
	[ 13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7 ],
	[ 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2 ],
	[ 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8 ],
	[ 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11 ]]

	# 将48位数据划分为8块用于s盒替换
	def split(string):
		splited = []
		for i in range(8):
			splited.append(string[i * 6:i * 6 + 6])
		return splited

	temp = split(temp)
	result = []
	for i in range(8):
		column = int(temp[i][0] + temp[i][5],2)						# 行数
		row = int(temp[i][1]+temp[i][2]+temp[i][3]+temp[i][4], 2)	# 列数
		output = s[i+1][column][row]								# 查表
		output = bin(output).replace('0b','')
		while len(output) < 4:										# 不够4位的前面添0
			output = '0' + output
		output = list(output)
		result += output
	# type(result) = list
	return result
	
# p盒置换
def pBox(source):
	result = [0] * 32
	pbox = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31,
	10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25 ]
	for i in range(32):
		result[i] = source[pbox[i] - 1]
	return result

# 轮函数
def roundFun(data, key):
	# 异或每位
	def xor(temp, key):
		result = [0] * len(temp)
		for i in range(len(temp)):
			if temp[i] == key[i]:
				result[i] = '0'
			else: result[i] = '1'
		return result

	# 分左右片 输入右片 = 输出的左片
	dataLeft = data[:32]
	dataRight = leftResult = data[32:]
	# f函数
	temp = expend(dataRight)
	temp = xor(temp, key)
	temp = sBox(temp)
	temp = pBox(temp)
	rightResult = xor(temp, dataLeft)
	result = leftResult + rightResult
	return result

# 扩展置换
def expend(source):
	result = [0] * 48
	# E盒
	expendBox = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12,
	13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22,
	23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1 ]
	for i in range(48):
		result[i] = source[expendBox[i] - 1]
	return result


# 循环左移56位密钥
def roundKey(key, count):
	# 根据位移的轮数选择位移数
	rotate = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
	# 按位移数移位  k > 0 左移
	def rotation(lst, k):
		return lst[k:] + lst[:k]

	keyLeft = key[:28]
	keyRight = key[28:]			# 分片
	k = rotate[count - 1]
	keyLeft  = rotation(keyLeft , k)	# 根据轮次移位
	keyRight = rotation(keyRight, k)
	key = keyLeft + keyRight
	return key

# 置换选择1
def keyPC_1(key):
	# 将十六进制的key转为二进制的list
	key = bin(key).replace('0b','')
	while len(key) < 64:
		key = '0' + key
	# 通过置换选择1得到有效的56位密钥
	result = [0] * 56
	pc1 = [57, 49, 41, 33, 25, 17, 9,
	1, 58, 50, 42, 34, 26, 18,
	10,  2, 59, 51, 43, 35, 27,
	19, 11,  3, 60, 52, 44, 36,
	63, 55, 47, 39, 31, 23, 15,
	7, 62, 54, 46, 38, 30, 22,
	14,  6, 61, 53, 45, 37, 29,
	21, 13,  5, 28, 20, 12,  4 ]
	# 按位置换
	for i in range(56):
		result[i] = key[pc1[i] - 1]
	return result

# 通过置换选择2压缩为48位密钥
def keyPC_2(source):
	result = [0] * 48
	pc2 = [14, 17, 11, 24, 1, 5,
	3, 28, 15,  6, 21, 10,
	23, 19, 12,  4, 26,  8,
	16,  7, 27, 20, 13,  2,
	41, 52, 31, 37, 47, 55,
	30, 40, 51, 45, 33, 48,
	44, 49, 39, 56, 34, 53,
	46, 42, 50, 36, 29, 32 ]
	for i in range(48):
		result[i] = source[pc2[i] - 1]
	return result

# 逆初始置换
def endExchange(data):
	result = [0] * 64
	# 逆初始置换盒
	_ip = [
	40, 8, 48, 16, 56, 24, 64, 32, 39, 7,47, 15, 55, 23, 63, 31,
	38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45,13, 53, 21, 61, 29,
	36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11,51, 19, 59, 27,
	34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
	for i in range(64):
		result[i] = data[_ip[i] - 1]
	return result

def DES(data, key):
	# 对64位key进行置换选择1
	key = keyPC_1(key)		# 置换选择1

	# 对64位data进行初始置换
	data = initExchange(data)

	# 进行16轮轮函数操作
	for i in range(16):
		key = roundKey(key, i + 1)
		keyUse = keyPC_2(key)
		data = roundFun(data, keyUse)

	# 经过16轮的加密之后，最后一轮的左右调换就是结果
	dataLeft = data[:32]
	dataRight = data[32:]
	data = dataRight + dataLeft
	# 逆初始置换
	data = endExchange(data)
	# 以一定的格式输出
	data = ''.join(data)
	data = int('0b' + data, 2)
	# 以十进制输出
	return data

# 解密过程
def DESre(data, key):
	key2 = keyPC_1(key)
	data = initExchange(data)
	# 解密的过程密钥顺序是加密的调转，k1=_k16 k2=_k15 ...
	for i in range(16):
		key3 = key2
		for j in range(16 - i):
			key3 = roundKey(key3, j + 1)
		keyUse = keyPC_2(key3)
		data = roundFun(data, keyUse)

	dataLeft = data[:32]
	dataRight = data[32:]
	data = dataRight + dataLeft
	data = endExchange(data)

	# 以一定的格式输出
	data = ''.join(data)
	data = int('0b' + data, 2)
	# 以十进制输出
	return data
	