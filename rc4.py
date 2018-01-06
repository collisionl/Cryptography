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

if __name__ == '__main__':
	# key必须为128bit
	key = '3CA10B2157F01916902E1380ACC107BD'
	# plain为hex的数据 2个hex代表一个字节
	plain = '47726f756e6420436f6e74726f6c2074'	

	# 扩展原密钥生成S盒
	expansion_key = KSA(key)
	# print (expansion_key)

	# 根据text长度生成定长的密钥流
	text_len = int(len(plain) / 2)
	gen_key = PRGA(expansion_key, text_len)

	cipher = RC4(gen_key, plain, text_len)
	print (cipher)

	plain2 = RC4(gen_key, cipher, text_len)
	print (plain2)



# Ground Control t
# 0x47726f756e6420436f6e74726f6c2074