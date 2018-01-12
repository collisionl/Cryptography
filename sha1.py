# coding:utf-8
def init(text):
	bin_text = ''
	for i in range(len(text)):
		temp = bin(ord(text[i]))[2:]
		while len(temp) < 8: 
			temp = '0' + temp
		bin_text += temp
	len_bin_text = bin(len(bin_text))[2:]
	while len(len_bin_text) < 64:
		len_bin_text = '0' + len_bin_text
	if len(bin_text) % 512 != 448:
		bin_text = bin_text + '1'
		while len(bin_text) % 512 != 448:
			bin_text = bin_text + '0'
	return bin_text + len_bin_text

def left_shift(temp, shift):
	temp = temp & 0xffffffff
	return (temp << shift) | (temp >> (32 - shift))

# 扩充m数组
def expansion_of_m(text_listi):
	# 分组
	m = [0 for i in range(80)]
	for i in range(16):
		m[i] = int(text_listi[i*32:i*32+32], 2)
	# 扩充
	for i in range(16,80):
		temp = m[i-16] ^ m[i-14] ^ m[i-8] ^ m[i-3]
		m[i] = left_shift(temp, 1)
	return m

# 压缩函数
def compress_fun(text_listi, i, round_result):
	def ch(x, y, z): return (x & y) ^ (~x & z)
	def pa(x, y, z): return x ^ y ^ z
	def ma(x, y, z): return (x & y) ^ (x & z) ^ (y & z)
	if i == 0:
		a = 0x67452301
		b = 0xEFCDAB89
		c = 0x98BADCFE
		d = 0x10325476
		e = 0xC3D2E1F0
	else:
		a = int(round_result[:8], 16)
		b = int(round_result[8:16], 16)
		c = int(round_result[16:24], 16)
		d = int(round_result[24:32], 16)
		e = int(round_result[32:], 16)
	aa = a
	bb = b
	cc = c
	dd = d
	ee = e
	# 扩充
	m = expansion_of_m(text_listi)
	# 第一步
	for i in range(20):
		temp_a = (left_shift(a, 5) + ch(b, c, d) + e + m[i] + 0x5A827999) & 0xffffffff
		temp_b = a
		temp_c = left_shift(b, 30) & 0xffffffff
		temp_d = c
		temp_e = d
		a = temp_a
		b = temp_b
		c = temp_c
		d = temp_d
		e = temp_e
	# 第二步
	for i in range(20):
		temp_a = (left_shift(a, 5) + pa(b, c, d) + e + m[i+20] + 0x6ED9EBA1) & 0xffffffff
		temp_b = a
		temp_c = left_shift(b, 30) & 0xffffffff
		temp_d = c
		temp_e = d
		a = temp_a
		b = temp_b
		c = temp_c
		d = temp_d
		e = temp_e
	# 第三步
	for i in range(20):
		temp_a = (left_shift(a, 5) + ma(b, c, d) + e + m[i+40] + 0x8F1BBCDC) & 0xffffffff
		temp_b = a
		temp_c = left_shift(b, 30) & 0xffffffff
		temp_d = c
		temp_e = d
		a = temp_a
		b = temp_b
		c = temp_c
		d = temp_d
		e = temp_e
	# 第四步
	for i in range(20):
		temp_a = (left_shift(a, 5) + pa(b, c, d) + e + m[i+60] + 0xCA62C1D6) & 0xffffffff
		temp_b = a
		temp_c = left_shift(b, 30) & 0xffffffff
		temp_d = c
		temp_e = d
		a = temp_a
		b = temp_b
		c = temp_c
		d = temp_d
		e = temp_e
	a = hex((aa + a) & 0xffffffff)[2:]
	while len(a) < 8: a = '0' + a
	b = hex((bb + b) & 0xffffffff)[2:]
	while len(b) < 8: b = '0' + b
	c = hex((cc + c) & 0xffffffff)[2:]
	while len(c) < 8: c = '0' + c
	d = hex((dd + d) & 0xffffffff)[2:]
	while len(d) < 8: d = '0' + d
	e = hex((ee + e) & 0xffffffff)[2:]
	while len(e) < 8: e = '0' + e
	return a + b + c + d + e

def sha1(text):
	text_list = [0 for i in range(int(len(text)/512))]
	for i in range(int(len(text)/512)):
		text_list[i] = text[i*512:i*512+512]
	round_result = 0
	for i in range(len(text_list)):
		round_result = compress_fun(text_list[i], i, round_result)
	return round_result.upper()

if __name__ == '__main__':
	# text = 'iscbupt'
	# text = 'asjfljshdflkjhasdlkjfhasdkljfhaskldjfhaklsjdhfkljasdhfkljsahdfjklashdfjlkshadljkfhlskadfjk'
	# text = 'Beijing University of Posts and Telecommunications'
	# text = 'State Key Laboratory of Networking and Switching'
	fileopen = open('infile.txt','r+')
	text = fileopen.read()
	fileopen.close()

	format_text = init(text)
	result = sha1(format_text)
	print (result)