# coding:utf-8

# format the input
def init(text):
	# tran to bin
	bin_text = ''
	for i in range(len(text)):
		temp = bin(ord(text[i]))[2:]
		while len(temp) < 8: 
			temp = '0' + temp
		bin_text += temp
	# cal the len of text and padding with 0 in the front
	len_bin_text = bin(len(bin_text))[2:]
	while len(len_bin_text) < 64:
		len_bin_text = '0' + len_bin_text
	# padding with 100... if mod != 448
	if len(bin_text) % 512 != 448:
		bin_text = bin_text + '1'
		while len(bin_text) % 512 != 448:
			bin_text = bin_text + '0'

	return bin_text + len_bin_text

def compress_fun(text_list, i, round_result):
	if i == 0:
		a = 0x67452301
		b = 0xEFCDAB89
		c = 0x98BADCFE
		d = 0x10325476
	else:
		a = round_result[:32]
		b = round_result[32:64]
		c = round_result[64:96]
		d = round_result[96:]
	aa = a
	bb = b
	cc = c
	dd = d

	# print (text_list)
	m = [0 for i in range(16)]
	for i in range(16):
		m[i] = text_list[i*32:i*32+32]
	# print (m)
	


def md5(text):
	# print (text)
	text_list = [0 for i in range(int(len(text)/512))]
	for i in range(int(len(text)/512)):
		text_list[i] = text[i*512:i*512+512]
	round_result = 0
	for i in range(len(text_list)):
		round_result = compress_fun(text_list[i], i, round_result)



if __name__ == '__main__':
	text = 'iscbupt'
	format_text = init(text)
	md5(format_text)