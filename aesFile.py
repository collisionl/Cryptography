from aes import *

def str2bin(string):
	result = ''
	for i in string:
		temp = bin(ord(i))[2:]
		while len(temp) < 8:
			temp = '0' + temp
		result += temp
	return result

def bin2str(string):
	result = ''
	for i in range(16):
		temp = string[i*8:i*8+8]
		temp = chr(int(temp,2))
		result += temp
	return result

def AESfile(filepath, key):
	with open(filepath , 'r+') as fd:
		result = ''
		while True:
			part = fd.read(16)
			if len(part) == 0: break
			part = str(part)
			part = str2bin(part)
			part = int(part,2)
			partaes = AES(part, key)
			partaes = hex(partaes)[2:]
			while len(partaes) < 32:
				partaes = '0' + partaes
			result += partaes
		# print (result)

	with open('aes_encryptfile.txt', 'w+') as of:
		of.write(result)
		print ('Done')

def _AESfile(filepath, key):
	with open(filepath , 'r+') as fd:
		result = ''
		while True:
			part = fd.read(32)
			if len(part) == 0: break
			partaes = inv_AES(int(part,16), key)
			partaes = bin(partaes)[2:]
			while len(partaes) < 128:
				partaes = '0' + partaes
			partresult = bin2str(partaes)
			result += partresult
		# print (result)

	with open('aes_decryptfile.txt', 'w+') as of:
		of.write(result)
		print ('Done')


if __name__ == '__main__':
	key = 0x3CA10B2157F01916902E1380ACC107BD
	filepathin = 'infile.txt'
	filepathout = 'aes_encryptfile.txt'
	AESfile(filepathin, key)
	_AESfile(filepathout, key)
	



