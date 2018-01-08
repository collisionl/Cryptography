# coding:utf-8
def key_gen(key, lenofplain):
	def shift(x_list, x):
		if x == 'a':
			temp = str(int(x_list[13]) ^ int(x_list[16]) ^ int(x_list[17]) ^ int(x_list[18]))
		elif x == 'b':
			temp = str(int(x_list[12]) ^ int(x_list[16]) ^ int(x_list[20]) ^ int(x_list[21]))
		else:
			temp = str(int(x_list[17]) ^ int(x_list[18]) ^ int(x_list[21]) ^ int(x_list[22]))
		result = [0 for i in range(len(x_list))]
		for i in range(len(x_list) - 1,0, -1):
			result[i] = x_list[i - 1]
		result[0] = temp
		result = ''.join(result)
		return result

	key_list = bin(key)[2:]
	while key_list < 64:
		key_list = '0' + key_list
	a_init = key_list[:19]
	b_init = key_list[19:41]
	c_init = key_list[41:]

	a_list = a_init
	b_list = b_init
	c_list = c_init
	result = [0 for i in range(lenofplain)]
	for i in range(lenofplain):
		x = int(a_list[9])
		y = int(b_list[11])
		z = int(c_list[11])
		if x+y+z >= 2:
			if x == 1:
				a_list = shift(a_list, 'a')
			if y == 1:
				b_list = shift(b_list, 'b')
			if z == 1:
				shift(c_list, 'c')
		else:
			if x == 0:
				a_list = shift(a_list, 'a')
			if y == 0:
				b_list = shift(b_list, 'b')
			if z == 0:
				c_list = shift(c_list, 'c')
		result[i] = str(int(a_list[18]) ^ int(b_list[21]) ^ int(c_list[22]))
	result = ''.join(result)
	return result

def a5_file(filepath, key):
	fileread = open(filepath, 'r+')
	data = fileread.read()
	fileread.close()
	filetexthex = ''
	for i in range(len(data)):
		temp = bin(ord(data[i]))[2:]
		while len(temp) < 8: 
			temp = '0' + temp
		filetexthex += temp
	lenofplain = len(filetexthex)
	gen_key = key_gen(key, lenofplain)
	cipher = int(filetexthex, 2) ^ int(gen_key, 2)
	cipherbin = bin(cipher)[2:]
	while len(cipherbin) < lenofplain:
		cipherbin = '0' + cipherbin
	cipherprint = hex(cipher)[2:].replace('L','')

	filewrite = open('a5enctypt.txt', 'w+')
	filewrite.write(cipherprint)
	filewrite.close()
	print ('Done')
	
def inv_a5_file(filepath, key):
	fileread = open(filepath, 'r+')
	data = fileread.read()
	fileread.close()

	lenofcipher = len(data) * 4
	gen_key = key_gen(key, lenofcipher)
	plain = int(data, 16) ^ int(gen_key, 2)
	plainhex = hex(plain)[2:].replace('L','')

	plain = ''
	for i in range(len(plainhex)/2):
		temp = plainhex[i*2:i*2+2]
		temp = chr(int(temp,16))
		plain += temp

	filewrite = open('a5dectypt.txt', 'w+')
	filewrite.write(plain)
	filewrite.close()
	print ('Done')


if __name__ == '__main__':
	key = 0xfC9129ff57F01116
	filepath = 'randomfile.txt'
	a5_file(filepath, key)
	filepath2 = 'a5enctypt.txt'
	inv_a5_file(filepath2, key)	