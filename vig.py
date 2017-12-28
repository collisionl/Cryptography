# coding = utf-8
def Encryption():
	plainText = input('input plainText:\n')
	plainText = plainText.lower()
	key = input('input key:\n')
	key = key.lower()
	# 如果key不够长，扩展key的长度直到比plainTextList长
	while len(plainText) > len(key): key += key

	cipherText = ''
	for (plainItem, keyItem) in zip(plainText, key):
		# 先给plainText和key中元素减去'a'的ascii码，然后相加并模26，再加上'a'的ascii码，最后int转为char
		cipherText += chr(((ord(plainItem) - 97 + ord(keyItem) - 97) % 26) + 97)
	print ('cipher is:', cipherText.upper())


def Decryption():
	cipherText = input('input cipherText\n')
	cipherText = cipherText.lower()		# 转为小写
	key = input('input key:\n')
	key = key.lower()
	while len(cipherText) > len(key): key += key

	plainText = ''
	for (plainItem, keyItem) in zip(cipherText, key):
		# 求密文减key的差值，不需要减去'a'的ascii码，然后取模再加上'a'的ascii码，最后int转为char
		plainText += chr(((ord(plainItem) - ord(keyItem))) % 26 + 97)
	print ('plain is:', plainText)



# 求出密钥长度
def lenOfKey(string):
	minDiff = 0x7fffffff
	length = 0
	for part in range(1, 10):
		# print (part)
		splited = split(string, part)			# 按分组个数划分密文，splited为划分好的几个分组组成的list
		# print (splited)
		sumPoss = 0
		for eachPart in range(part):			# 在划分好的密文分组中，每一个分组求概率，然后相加
			sumPoss += cal(splited[eachPart])

		diff = abs(sumPoss/part - 0.065)		# 求出在不同的划分下，平均的重合指数值，然后算出和标准0.065的偏差的绝对值
		if diff < minDiff:						# 找出最小偏差的划分，即是密钥长度
			minDiff = diff
			length = part
	return length

# 按照传入参数part，划分part个分组
def split(string, part):
	splited = []
	for i in range(part):						# 划分密文，并将每组划分存入splited
		splited.append(string[i::part])			# i：从下标i开始，part：每格part长度选取
	return splited

# 将每个划分好的字符串求出各自的重合指数值
def cal(splitedString):
	sum = 0
	alphabet = [chr(i+97) for i in range(26)]
	for letter in alphabet:						# 计算字符串中每个字母的出现概率
		letterProb = splitedString.count(letter)
		letterProb = letterProb * (letterProb - 1)	# sum(0-25)(fi*(fi-1))
		sum += letterProb
	allSum = len(splitedString) * (len(splitedString) - 1)	# n*(n-1)
	return sum / allSum										# Ic = sum(0-25)(fi*(fi-1)) / n*(n-1)
	
# 计算得出key
def getKey(string, part):
	splited = split(string, part)
	# 英文单词统计概率
	dict = {'A':0.082,'B':0.015,'C':0.028,'D':0.043,'E':0.127,'F':0.022,'G':0.02,'H':0.061,'I':0.07,\
	'J':0.002,'K':0.008,'L':0.04,'M':0.024,'N':0.067,'O':0.075,'P':0.019,'Q':0.001,'R':0.060,'S':0.063,\
	'T':0.091,'U':0.028,'V':0.010,'W':0.023,'X':0.001,'Y':0.020,'Z':0.001}
	# 小写字母表
	alphabet = [chr(i+97) for i in range(26)]
	key = ''
	for i in range(len(splited)):
		arrayOfPro = []
		for n in range(0, 26):
			tra = trans(splited[i], n)							# 右移n位
			p = 0
			for letter in alphabet:
				# 每个字母重合指数相加
				p = p + tra.count(letter) * dict[letter.upper()] / len(tra)
			arrayOfPro.append(abs(p - 0.065))					# 与标准概率比对
		key += chr(arrayOfPro.index(min(arrayOfPro)) + 97)		# 取差值最小的拼成key
	return key

# 移位操作
def trans(string, n):
	newstring = ''
	# 将字符串中每个字符右移n位
	for letter in string:
		newstring += chr((ord(letter) - 97 - n) % 26 + 97 )	
	return newstring

def bruteForce():
	cipherText = input('input cipherText\n')
	cipherText = cipherText.lower()		# 转为小写
	length = lenOfKey(cipherText)		# 得到长度
	key = getKey(cipherText, length)
	print ('key is:', key.upper())
	# 使用求出的key解密
	while len(cipherText) > len(key): key += key
	plainText = ''
	for (plainItem, keyItem) in zip(cipherText, key):
		plainText += chr(((ord(plainItem) - ord(keyItem))) % 26 + 97)
	print ('plain is:', plainText)



if __name__ == '__main__':
	a = int(input('Encryption type 1, Decryption type 2, bruteForce type 3\n'))
	if a == 1:
		Encryption()
	elif a == 2:
		Decryption()
	else:
		bruteForce()

# 1
# cybergreatwallcorporation
# iscbupt
# kqdflvkmsvxuaekgtqigtbaqo

# 2
# THEBUTCHERTHEBAKERANDTHECANDLESTICKMAKER
# BIG
# UPKCCZDPKSBNFJGLMXBVJUPKDITETKTBODSSBSKS

# 3
# CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBJJCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE
# janet
# thealmondtreewasintentativeblossomthedayswerelongeroftenendingwithmagnificenteveningsofcorrugatedpinkskiesthehuntingseasonwasoverwithhoundsandgunsputawayforsixmonthsthevineyardswerebusyagainasthewellorganizedfarmerstreatedtheirvinesandthemorelackadaisicalneighborshurriedtofqthepruningtheyshouldhavedoneinnovember

# 4
# KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST
# crypto
# ilearnedhowtocalculatetheamountofpaperneededforaroomwheniwasatschoolyoumultiplythesquarefootageofthewallsbythecubiccontentsofthefloorandceilingcombinedanddoubleityouthenallowhalfthetotalforopeningssuchaswindowsanddoorsthenyouallowtheotherhalfformatchingthepatternthenyoudoublethewholethingagaintogiveamarginoferrorandthenyouorderthepaper

# 5
# koommacomoqeglxxmqcckueyfcurylyligzsxczvbckmyopnpogdgiaztxddiaknvomxhiemrdezvxbmzrnlzayqiqxgkkkpnevhovvbkktcssepkgdhxyvjmrdkbcjuefmakntdrxbiemrdprrjbxfqnemxdrlbcjhpztvvixyetniiawdrgnomrzrreikioxrusxcretvzaozygyukndwpiouoriyrhhbzxrceayvxuvrxkcmaxstxsepbrxcs1rukvbxtgzuggdwhxmxcsxbiktnslrjzhbxmspungzrgkudxnaufcmrzxjrywymi
# GTKZENR
# eveninliteraturecryptologyhassometimesaroletoplayinthenineteenthcenturytheamericanauthoredgarallanpoewroteastoryentitledthegoldbuginthatstorytheleadingmangetsholdofapieceofparchmentwithanencryptedmessagetheauthordescribeselaboratelyhowtheleadingmantacklestgedecryptionwesuggesttoreadthestoryifyouwanttoknowhowthatwasdone







