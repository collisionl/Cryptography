from des import *

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
	for i in range(8):
		temp = string[i*8:i*8+8]
		temp = chr(int(temp,2))
		result += temp
		# print (temp)
	return result

def DESfile(filepath, key):
	with open(filepath , 'r+') as fd:
		result = ''
		while True:
			part = fd.read(8)
			if len(part) == 0: break
			part = str(part)
			part = str2bin(part)
			part = int(part,2)
			# print (hex(part))
			partdes = DES(part, key)
			partdes = hex(partdes)[2:]
			# print (partdes)
			while len(partdes) < 16:
				partdes = '0' + partdes
			result += partdes
			# print (partresult)
		# print (result)

	with open('des_encryptfile.txt', 'w+') as of:
		of.write(result)
		print ('Done')

def _DESfile(filepath, key):
	with open(filepath , 'r+') as fd:
		result = ''
		while True:
			part = fd.read(16)
			if len(part) == 0: break
			part = str(part)
			part = int(part, 16)
			partdes = DESre(part, key)
			partdes = bin(partdes)[2:]
			while len(partdes) < 64:
				partdes = '0' + partdes
			partresult = bin2str(partdes)
			result += partresult
		# print (result)

	with open('des_decryptfile.txt', 'w+') as of:
		of.write(result)
		print ('Done')


if __name__ == '__main__':
	key = 0x0E329232EA6A0D73
	filepathin = 'infile.txt'
	filepathout = 'des_encryptfile.txt'
	DESfile(filepathin, key)
	_DESfile(filepathout, key)
	
