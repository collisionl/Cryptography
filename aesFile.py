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
		# print (temp)
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
			# print (hex(part), '1')
			partaes = AES(part, key)
			# print (hex(partaes), '2')
			partaes = bin(partaes)[2:]
			while len(partaes) < 128:
				partaes = '0' + partaes
			partresult = bin2str(partaes)
			result += partresult
		# print (result)

	with open('aes_encryptfile.txt', 'w+') as of:
		of.write(result)
		print ('Done')

def _AESfile(filepath, key):
	with open(filepath , 'r+') as fd:
		result = ''
		while True:
			part = fd.read(16)
			if len(part) == 0: break
			part = str(part)
			# print (part)
			part = str2bin(part)
			part = int(part,2)
			# print (hex(part), '3')
			partaes = inv_AES(part, key)
			# print (hex(partaes), '4')
			partaes = bin(partaes)[2:]
			while len(partaes) < 128:
				partaes = '0' + partaes
			partresult = bin2str(partaes).replace('b\'','')
			result += partresult
		# print (result)

	with open('aes_decryptfile.txt', 'w+') as of:
		of.write(result)
		print ('Done')


if __name__ == '__main__':
	key = 0x3CA10B2157F01916902E1380ACC107BD
	filepathin = 'dec1.txt'
	filepathout = 'aes_encryptfile.txt'
	AESfile(filepathin, key)
	_AESfile(filepathout, key)
	



