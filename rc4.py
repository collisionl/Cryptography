# coding:utf-8
def KSA(key):
	key_list = [0 for i in range(16)]
	for i in range(16):
		key_list[i] = int(key[i*2:i*2+2], 16)
	S = [i for i in range(256)]
	T = [0 for i in range(256)]
	for i in range(256):
		T[i] = key_list[i % 16]
	j = 0 
	for i in range(256):
		j = (j + S[i] + T[i]) % 256
		temp = S[i]
		S[i] = S[j]
		S[j] = temp
	return S

def PRGA(expansion_key, text_len):
	key = [expansion_key[i] for i in range(256)]
	i = j = count = 0
	k = [0 for i in range(text_len)]
	while count < text_len:
		i = (i + 1) % 256
		j = (j + key[i]) % 256
		temp = key[i]
		key[i] = key[j]
		key[j] = temp
		t = (key[i] + key[j]) % 256
		k[count] = key[t]
		count += 1
	return k

def RC4(gen_key, plain, text_len):
	plain_list = [0 for i in range(text_len)]
	cipher_list = [0 for i in range(text_len)]
	cipher = ''
	for i in range(text_len):
		plain_list[i] = int(plain[i*2:i*2+2], 16)
		cipher_list[i] = hex(plain_list[i] ^ gen_key[i])[2:]
		if len(cipher_list[i]) < 2:
			cipher_list[i] = '0' + cipher_list[i]
		cipher += ''.join(cipher_list[i])
	return cipher

def file_RC4(key, filepath):
	# 扩展原密钥生成S盒
	expansion_key = KSA(key)

	fileopen = open(filepath, 'r+')
	filetext = fileopen.read()
	fileopen.close()
	filetextstr = ''
	for i in range(len(filetext)):
		temp = hex(ord(filetext[i]))[2:]
		if len(temp) < 2: temp = '0' + temp
		filetextstr += temp

	# 根据text长度生成定长的密钥流
	text_len = int(len(filetextstr) / 2)
	gen_key = PRGA(expansion_key, text_len)
	# 加密
	cipher = RC4(gen_key, filetextstr, text_len)
	
	fileopen2 = open('RC4encryptfile.txt', 'w+')
	fileopen2.write(cipher)
	fileopen2.close()
	print ('Done')

def inv_file_RC4(key, filepath):
	# 扩展原密钥生成S盒
	expansion_key = KSA(key)

	fileopen = open(filepath, 'r+')
	filetext = fileopen.read()
	fileopen.close()
	filetextstr = filetext

	text_len = int(len(filetextstr) / 2)
	gen_key = PRGA(expansion_key, text_len)
	plainstr = RC4(gen_key, filetextstr, text_len)

	plain = ''
	for i in range(text_len):
		temp = plainstr[i*2:i*2+2]
		temp = chr(int(temp,16))
		plain += temp
	
	fileopen2 = open('RC4decryptfile.txt', 'w+')
	fileopen2.write(plain)
	fileopen2.close()
	print ('Done')

if __name__ == '__main__':
	# key必须为128bit
	key = '3CA10B2157F01916902E1380ACC107BD'

	filepath = 'infile.txt'
	file_RC4(key, filepath)
	filepath = 'RC4encryptfile.txt'
	inv_file_RC4(key, filepath)
