s_box = [
	#  0     1     2     3     4     5     6     7     8     9     a     b     c     d     e     f
	[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76], #  0
	[0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0], #  1
	[0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15], #  2
	[0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75], #  3
	[0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84], #  4
	[0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf], #  5
	[0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8], #  6
	[0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2], #  7
	[0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73], #  8
	[0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb], #  9
	[0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79], #  a
	[0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08], #  b
	[0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a], #  c
	[0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e], #  d
	[0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf], #  e
	[0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]] #  f

inv_s_box = [
	#  0     1     2     3     4     5     6     7     8     9     a     b     c     d     e     f
	[0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb], #  0
	[0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb], #  1
	[0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e], #  2
	[0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25], #  3
	[0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92], #  4
	[0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84], #  5
	[0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06], #  6
	[0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b], #  7
	[0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73], #  8
	[0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e], #  9
	[0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b], #  a
	[0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4], #  b
	[0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f], #  c
	[0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef], #  d
	[0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61], #  e
	[0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]] #  f

# 将输入明文转为数组形式存储
def format(plain):
	plain = str(hex(plain))[2:]
	while len(plain) < 32:
		plain = '0' + plain
	plainlist = [[0 for i in range(4)] for j in range(4)]
	for i in range(4):
		for j in range(4):
			plainlist[i][j] = plain[2*i+8*j:2*i+8*j+2]
	return plainlist

# 字节代换
def sub_bytes(plainlist):
	result = [[0 for i in range(4)] for j in range(4)]
	for i in range(4):
		for j in range(4):
			onebyte = plainlist[i][j]
			row = int(onebyte[0], 16)
			col = int(onebyte[1], 16)
			temp = hex(s_box[row][col])[2:]
			if len(temp) < 2: temp = '0' + temp
			result[i][j] = temp
	return result

# 逆字节代换
def inv_sub_bytes(plainlist):
	result = [[0 for i in range(4)] for j in range(4)]
	for i in range(4):
		for j in range(4):
			onebyte = plainlist[i][j]
			row = int(onebyte[0], 16)
			col = int(onebyte[1], 16)
			temp = hex(inv_s_box[row][col])[2:]
			if len(temp) < 2: temp = '0' + temp
			result[i][j] = temp
	return result

# 行移位
def shift_rows(plainlist):
	temp10 = plainlist[1][0]
	plainlist[1][0] = plainlist[1][1]
	plainlist[1][1] = plainlist[1][2]
	plainlist[1][2] = plainlist[1][3]
	plainlist[1][3] = temp10

	temp20 = plainlist[2][0]
	temp21 = plainlist[2][1]
	plainlist[2][0] = plainlist[2][2]
	plainlist[2][1] = plainlist[2][3]
	plainlist[2][2] = temp20
	plainlist[2][3] = temp21

	temp33 = plainlist[3][3]
	plainlist[3][3] = plainlist[3][2]
	plainlist[3][2] = plainlist[3][1]
	plainlist[3][1] = plainlist[3][0]
	plainlist[3][0] = temp33
	return plainlist

# 逆行移位
def inv_shift_rows(plainlist):
	temp13 = plainlist[1][3]
	plainlist[1][3] = plainlist[1][2]
	plainlist[1][2] = plainlist[1][1]
	plainlist[1][1] = plainlist[1][0]
	plainlist[1][0] = temp13

	temp20 = plainlist[2][0]
	temp21 = plainlist[2][1]
	plainlist[2][0] = plainlist[2][2]
	plainlist[2][1] = plainlist[2][3]
	plainlist[2][2] = temp20
	plainlist[2][3] = temp21

	temp30 = plainlist[3][0]
	plainlist[3][0] = plainlist[3][1]
	plainlist[3][1] = plainlist[3][2]
	plainlist[3][2] = plainlist[3][3]
	plainlist[3][3] = temp30
	return plainlist

# 列混合
def mix_column(plainlist):
	# 根据gf(2^8)上的乘二法则运算 page97 4-10
	def mul2(plainlist_item):
		plainlist_item = bin(plainlist_item)[2:]
		while len(plainlist_item) < 8:
			plainlist_item = '0' + plainlist_item
		temp = plainlist_item[1:] + '0'
		temp = int(temp,2)
		if plainlist_item[0] == '1':
			result = temp ^ 0b00011011
			return result
		else: return temp

	# 如果乘3 则为乘2然后与本身异或
	def multi(mat_item, plainlist_item):
		if mat_item == 1:
			return plainlist_item
		elif mat_item == 2:
			return mul2(plainlist_item)
		elif mat_item == 3:
			return mul2(plainlist_item) ^ plainlist_item

	matlist = [
	[0x02, 0x03, 0x01, 0x01],
	[0x01, 0x02, 0x03, 0x01],
	[0x01, 0x01, 0x02, 0x03],
	[0x03, 0x01, 0x01, 0x02]]

	# 16进制str 转 int
	for i in range(4):
		for j in range(4):
			plainlist[i][j] = int(plainlist[i][j], 16)

	# 矩阵乘法
	result = [[0 for i in range(4)] for j in range(4)]
	for i in range(4):
		for j in range(4):
			temp = 0x0
			for k in range(4):
				temp = temp ^ multi(matlist[i][k], plainlist[k][j])
			result[i][j] = temp

	# int 转 16进制str
	for i in range(4):
		for j in range(4):
			result[i][j] = hex(result[i][j])[2:]
			if len(result[i][j]) < 2:
				result[i][j] = '0' + result[i][j]

	return result

# 逆列混合
def inv_mix_column(plainlist):
	inv_matlist = [
	[0x0E, 0x0B, 0x0D, 0x09],
	[0x09, 0x0E, 0x0B, 0x0D],
	[0x0D, 0x09, 0x0E, 0x0B],
	[0x0B, 0x0D, 0x09, 0x0E]]
	def mul2(plainlist_item):
		plainlist_item = bin(plainlist_item)[2:]
		while len(plainlist_item) < 8:
			plainlist_item = '0' + plainlist_item
		temp = plainlist_item[1:] + '0'
		temp = int(temp,2)
		if plainlist_item[0] == '1':
			result = temp ^ 0b00011011
			return result
		else: return temp

	def mul4(plainlist_item):
		return mul2(mul2(plainlist_item))
	def mul8(plainlist_item):
		return mul2(mul2(mul2(plainlist_item)))

	# 乘9看做是乘8后与自己异或 (既偶数乘分解为多次乘2，奇数乘分解为多次偶数乘和自己异或)
	def multi(inv_matlist, plainlist_item):
		if inv_matlist == 0x09:
			return mul8(plainlist_item) ^ plainlist_item
		elif inv_matlist == 0x0B:
			return mul8(plainlist_item) ^ mul2(plainlist_item) ^ plainlist_item
		elif inv_matlist == 0x0D:
			return mul8(plainlist_item) ^ mul4(plainlist_item) ^ plainlist_item
		elif inv_matlist == 0X0E:
			return mul8(plainlist_item) ^ mul4(plainlist_item) ^ mul2(plainlist_item)

	for i in range(4):
		for j in range(4):
			plainlist[i][j] = int(plainlist[i][j], 16)

	result = [[0 for i in range(4)] for j in range(4)]
	for i in range(4):
		for j in range(4):
			temp = 0x0
			for k in range(4):
				temp = temp ^ multi(inv_matlist[i][k], plainlist[k][j])
			result[i][j] = temp

	for i in range(4):
		for j in range(4):
			result[i][j] = hex(result[i][j])[2:]
			if len(result[i][j]) < 2:
				result[i][j] = '0' + result[i][j]

	return result

# 轮密钥加，逆操作同样（异或的逆运算是本身）
def round_key_add(plainlist, round):
	w = [0 for i in range(4)]
	for i in range(4):
		w[i] = EXPANSIONED_KEY[4 * round + i]
	result = [[0 for i in range(4)] for j in range(4)]
	for i in range(4):
		for j in range(4):
			result[i][j] = int(w[j][i * 2:i * 2 + 2], 16) ^ int(plainlist[i][j], 16)
			result[i][j] = hex(result[i][j])[2:]
			if len(result[i][j]) < 2: result[i][j] = '0' + result[i][j]
	return result

# 轮密钥加的过程一致，但是在执行解密时，中间的9轮需要对密钥执行一次逆列混合
def inv_round_key_add(cipherlist, round):
	# 转格式
	def key_format(w):
		result = [[0 for i in range(4)] for j in range(4)]
		for i in range(4):
			for j in range(4):
				result[j][i] = w[i][j*2:j*2+2]
		return result
	def key_reformat(w):
		result = [0 for i in range(4)]
		for i in range(4):
			temp = ''
			for j in range(4):
				temp += ''.join(w[j][i])
				result[i] = temp
		return result

	w = [0 for i in range(4)]
	for i in range(4):
		w[i] = EXPANSIONED_KEY[4 * round + i]
	# 格式不一致，转为inv_mix_column需要的格式再执行，完成后reformat
	w = key_format(w)
	w = inv_mix_column(w)
	w = key_reformat(w)

	result = [[0 for i in range(4)] for j in range(4)]
	for i in range(4):
		for j in range(4):
			result[i][j] = int(w[j][i * 2:i * 2 + 2], 16) ^ int(cipherlist[i][j], 16)
			result[i][j] = hex(result[i][j])[2:]
			if len(result[i][j]) < 2: result[i][j] = '0' + result[i][j]
	return result

# 生成所有密钥
def key_expansion(input_key):
	# 轮常量
	rcon = [0x01000000, 0x02000000, 0x04000000, 0x08000000, 0x10000000,\
			0x20000000, 0x40000000, 0x80000000, 0x1b000000, 0x36000000]
	# T函数
	def t_fun(key_part, count):
		key_part = key_part[2:] + key_part[:2]
		key_temp = ''
		for i in range(0,7,2):
			row = int(key_part[i], 16) 
			col = int(key_part[i+1], 16)
			temp = hex(s_box[row][col])[2:]
			if len(temp) < 2: temp = '0' + temp
			key_temp += temp
		rc = rcon[count - 1]
		result = rc ^ int(key_temp ,16)
		result = hex(result)[2:]
		while len(result) < 8:
			result = '0' + result
		return result

	# 先将输入的key转为16进制的字符串
	input_key = str(hex(input_key))[2:]
	while len(input_key) < 32:
		input_key = '0' + input_key
	key = [[]] * 44
	# 初始化前4位位输入的值
	key[0] = input_key[0:8]
	key[1] = input_key[8:16]
	key[2] = input_key[16:24]
	key[3] = input_key[24:32]
	# 循环计算扩展的key值
	count = 0
	for i in range(4,44):
		# print (i)
		if i % 4 != 0:
			temp = int(key[i - 4], 16) ^ int(key[i - 1], 16)
			key[i] = hex(temp)[2:]
			while len(key[i]) < 8:
				key[i] = '0' + key[i]
		elif i % 4 == 0:
			count += 1
			temp = int(key[i - 4], 16) ^ int(t_fun(key[i - 1], count), 16)
			key[i] = hex(temp)[2:]
			while len(key[i]) < 8:
				key[i] = '0' + key[i]
	return key

# 将list转为str
def reformat(plainlist):
	cipher = ''
	for i in range(4):
		for j in range(4):
			cipher += ''.join(plainlist[j][i])
	cipher = '0x' + cipher
	return cipher

# AES加密
def AES(plain, key):
	global EXPANSIONED_KEY
	EXPANSIONED_KEY = key_expansion(key)
	# 读入后格式化为二维list
	plainlist = format(plain)
	# 先执行一轮轮密钥加
	plainlist = round_key_add(plainlist, 0)
	# 执行9轮加密
	for i in range(1, 10):
		plainlist = sub_bytes(plainlist)
		plainlist = shift_rows(plainlist)
		plainlist = mix_column(plainlist)
		plainlist = round_key_add(plainlist, i)
	# 最后一轮不执行列混合
	plainlist = sub_bytes(plainlist)
	plainlist = shift_rows(plainlist)
	plainlist = round_key_add(plainlist, 10)
	# 将list转为字符串
	cipher = reformat(plainlist)
	return int(cipher, 16)

# AES解密
def inv_AES(cipher, key):
	global EXPANSIONED_KEY
	EXPANSIONED_KEY = key_expansion(key)

	cipherlist = format(cipher)
	# 第一轮解密使用最后一轮密钥，直接调用轮密钥加
	cipherlist = round_key_add(cipherlist, 10)
	# 中间的9轮过程需要对密钥进行逆列混合之后再执行轮密钥加
	for i in range(9, 0, -1):
		cipherlist = inv_sub_bytes(cipherlist)
		cipherlist = inv_shift_rows(cipherlist)
		cipherlist = inv_mix_column(cipherlist)
		cipherlist = inv_round_key_add(cipherlist, i)
	# 最后一轮解密直接调用轮密钥加
	cipherlist = inv_sub_bytes(cipherlist)
	cipherlist = inv_shift_rows(cipherlist)
	cipherlist = round_key_add(cipherlist, 0)

	plain = reformat(cipherlist)
	return int(plain, 16)


	
