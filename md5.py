# coding:utf-8
# 转为md5需要的二进制表示
def init(text):
	bin_text = ''
	for i in range(len(text)):
		temp = bin(ord(text[i]))[2:]
		while len(temp) < 8: 
			temp = '0' + temp
		bin_text += temp
	# cal the len of text and padding with 0 in the front
	# 在填充后64位时（既总长度填充），实际操作中需要的数据不需转为小端续
	# 但其他数据需要转换，所以在初始换的时候直接将64位数据分32位各自转换
	# 运行时转换为原来的长度数值
	len_bin_text = bin(len(bin_text))[2:]
	while len(len_bin_text) < 32:
		len_bin_text = '0' + len_bin_text
	while len(len_bin_text) < 64:
		len_bin_text = len_bin_text + '0'
	# 左边既m[14]的32位
	left_of_text = int(len_bin_text[:32],2)
	left_of_text = endian_tran(left_of_text)
	left_of_text = (bin(left_of_text))[2:]
	while len(left_of_text) < 32:
		left_of_text = '0' + left_of_text
	# 右边既m[15]的32位
	right_of_text = int(len_bin_text[32:],16)
	right_of_text = endian_tran(right_of_text)
	right_of_text = bin(right_of_text)[2:]
	while len(right_of_text) < 32:
		right_of_text = '0' + right_of_text
	# 拼接成最终64位
	len_bin_text = left_of_text + right_of_text

	# 填充一个1和若干0
	if len(bin_text) % 512 != 448:
		bin_text = bin_text + '1'
		while len(bin_text) % 512 != 448:
			bin_text = bin_text + '0'

	return bin_text + len_bin_text

# 32位寄存器循环左移，左移前取低32位
def left_shift(temp, shift):
	temp = temp & 0xffffffff
	return (temp << shift) | (temp >> (32 - shift))

# 4个非线形函数
def f_fun(x, y, z): return (x & y) | ((~x) & z)
def g_fun(x, y, z): return (x & z) | (y & (~z))
def h_fun(x, y, z): return x ^ y ^ z
def i_fun(x, y, z): return y ^ (x | (~z))

# 步函数：因为32位寄存器，每次都取低32位
def step_f(a, b, c, d, mj, shift, ti):
	temp = a + f_fun(b, c, d) + mj + ti
	a = b + left_shift(temp, shift)
	return a & 0xffffffff
def step_g(a, b, c, d, mj, shift, ti):
	temp = a + g_fun(b, c, d) + mj + ti
	temp = temp & 0xffffffff
	a = b + left_shift(temp, shift)
	return a & 0xffffffff
def step_h(a, b, c, d, mj, shift, ti):
	temp = a + h_fun(b, c, d) + mj + ti
	temp = temp & 0xffffffff
	a = b + left_shift(temp, shift)
	return a & 0xffffffff
def step_i(a, b, c, d, mj, shift, ti):
	temp = a + i_fun(b, c, d) + mj + ti
	temp = temp & 0xffffffff
	a = b + left_shift(temp, shift)
	return a & 0xffffffff

# 大小端续转换
def endian_tran(num):
	temp = hex(num)[2:]
	while len(temp) < 8:
		temp = '0' + temp
	return int(temp[6:8]+temp[4:6]+temp[2:4]+temp[0:2], 16)

# 压缩函数
def compress_fun(text_listi, i, round_result):
	# 传入的text_listi仅为本次使用的512bit
	# i用来判断循环次数，第一次循环使用初始数据，否则使用上一次循环的结果
	if i == 0:
		a = 0x67452301
		b = 0xEFCDAB89
		c = 0x98BADCFE
		d = 0x10325476
	else:
		a = int(round_result[:8], 16)
		b = int(round_result[8:16], 16)
		c = int(round_result[16:24], 16)
		d = int(round_result[24:], 16)
	# 结束后与自己相加取模的备用
	aa = a
	bb = b
	cc = c
	dd = d
	# 512bit分片为16个32bit，并且转换端续
	m = [0 for z in range(16)]
	for j in range(16):
		m[j] = int(text_listi[j*32:j*32+32], 2)
		m[j] = endian_tran(m[j])
	# 第一轮
	a = step_f(a, b, c, d, m[0], 7, 0xd76aa478)
	d = step_f(d, a, b, c, m[1], 12, 0xe8c7b756)
	c = step_f(c, d, a, b, m[2], 17, 0x242070db)
	b = step_f(b, c, d, a, m[3], 22, 0xc1bdceee)
	a = step_f(a, b, c, d, m[4], 7, 0xf57c0faf)
	d = step_f(d, a, b, c, m[5], 12, 0x4787c62a)
	c = step_f(c, d, a, b, m[6], 17, 0xa8304613)
	b = step_f(b, c, d, a, m[7], 22, 0xfd469501)
	a = step_f(a, b, c, d, m[8], 7, 0x698098d8)
	d = step_f(d, a, b, c, m[9], 12, 0x8b44f7af)
	c = step_f(c, d, a, b, m[10], 17, 0xffff5bb1)
	b = step_f(b, c, d, a, m[11], 22, 0x895cd7be)
	a = step_f(a, b, c, d, m[12], 7, 0x6b901122)
	d = step_f(d, a, b, c, m[13], 12, 0xfd987193)
	c = step_f(c, d, a, b, m[14], 17, 0xa679438e)
	b = step_f(b, c, d, a, m[15], 22, 0x49b40821)
	# 第二轮
	a = step_g(a, b, c, d, m[1], 5, 0xf61e2562)
	d = step_g(d, a, b, c, m[6], 9, 0xc040b340)
	c = step_g(c, d, a, b, m[11], 14, 0x265e5a51)
	b = step_g(b, c, d, a, m[0], 20, 0xe9b6c7aa)
	a = step_g(a, b, c, d, m[5], 5, 0xd62f105d)
	d = step_g(d, a, b, c, m[10], 9, 0x2441453)
	c = step_g(c, d, a, b, m[15], 14, 0xd8a1e681)
	b = step_g(b, c, d, a, m[4], 20, 0xe7d3fbc8)
	a = step_g(a, b, c, d, m[9], 5, 0x21e1cde6)
	d = step_g(d, a, b, c, m[14], 9, 0xc33707d6)
	c = step_g(c, d, a, b, m[3], 14, 0xf4d50d87)
	b = step_g(b, c, d, a, m[8], 20, 0x455a14ed)
	a = step_g(a, b, c, d, m[13], 5, 0xa9e3e905)
	d = step_g(d, a, b, c, m[2], 9, 0xfcefa3f8)
	c = step_g(c, d, a, b, m[7], 14, 0x676f02d9)
	b = step_g(b, c, d, a, m[12], 20, 0x8d2a4c8a)
	# 第三轮
	a = step_h(a, b, c, d, m[5], 4, 0xfffa3942)
	d = step_h(d, a, b, c, m[8], 11, 0x8771f681)
	c = step_h(c, d, a, b, m[11], 16, 0x6d9d6122)
	b = step_h(b, c, d, a, m[14], 23, 0xfde5380c)
	a = step_h(a, b, c, d, m[1], 4, 0xa4beea44)
	d = step_h(d, a, b, c, m[4], 11, 0x4bdecfa9)
	c = step_h(c, d, a, b, m[7], 16, 0xf6bb4b60)
	b = step_h(b, c, d, a, m[10], 23, 0xbebfbc70)
	a = step_h(a, b, c, d, m[13], 4, 0x289b7ec6)
	d = step_h(d, a, b, c, m[0], 11, 0xeaa127fa)
	c = step_h(c, d, a, b, m[3], 16, 0xd4ef3085)
	b = step_h(b, c, d, a, m[6], 23, 0x4881d05)
	a = step_h(a, b, c, d, m[9], 4, 0xd9d4d039)
	d = step_h(d, a, b, c, m[12], 11, 0xe6db99e5)
	c = step_h(c, d, a, b, m[15], 16, 0x1fa27cf8)
	b = step_h(b, c, d, a, m[2], 23, 0xc4ac5665)
	# 第四轮
	a = step_i(a, b, c, d, m[0], 6, 0xf4292244)
	d = step_i(d, a, b, c, m[7], 10, 0x432aff97)
	c = step_i(c, d, a, b, m[14], 15, 0xab9423a7)
	b = step_i(b, c, d, a, m[5], 21, 0xfc93a039)
	a = step_i(a, b, c, d, m[12], 6, 0x655b59c3)
	d = step_i(d, a, b, c, m[3], 10, 0x8f0ccc92)
	c = step_i(c, d, a, b, m[10], 15, 0xffeff47d)
	b = step_i(b, c, d, a, m[1], 21, 0x85845dd1)
	a = step_i(a, b, c, d, m[8], 6, 0x6fa87e4f)
	d = step_i(d, a, b, c, m[15], 10, 0xfe2ce6e0)
	c = step_i(c, d, a, b, m[6], 15, 0xa3014314)
	b = step_i(b, c, d, a, m[13], 21, 0x4e0811a1)
	a = step_i(a, b, c, d, m[4], 6, 0xf7537e82)
	d = step_i(d, a, b, c, m[11], 10, 0xbd3af235)
	c = step_i(c, d, a, b, m[2], 15, 0x2ad7d2bb)
	b = step_i(b, c, d, a, m[9], 21, 0xeb86d391)
	# 结尾相加取余 不足8位补齐
	a = hex((a + aa) % (2**32))[2:]
	while len(a) < 8: a = '0' + a
	b = hex((b + bb) % (2**32))[2:]
	while len(b) < 8: b = '0' + b
	c = hex((c + cc) % (2**32))[2:]
	while len(c) < 8: c = '0' + c
	d = hex((d + dd) % (2**32))[2:]
	while len(d) < 8: d = '0' + d
	return a + b + c + d

# 结果转为大端续
def result_endian_tran(temp):
	return temp[6:8]+temp[4:6]+temp[2:4]+temp[0:2]
def deformat_result(result):
	return result_endian_tran(result[:8]) + result_endian_tran(result[8:16]) + \
		result_endian_tran(result[16:24]) + result_endian_tran(result[24:])

def md5(text):
	text_list = [0 for i in range(int(len(text)/512))]
	for i in range(int(len(text)/512)):
		text_list[i] = text[i*512:i*512+512]
	round_result = 0
	for i in range(len(text_list)):
		round_result = compress_fun(text_list[i], i, round_result)
	round_result = deformat_result(round_result).upper()
	print (round_result)

if __name__ == '__main__':
	# text = 'iscbupt'
	text = 'Beijing University of Posts and Telecommunications'
	# text = 'State Key Laboratory of Networking and Switching'
	format_text = init(text)
	md5(format_text)