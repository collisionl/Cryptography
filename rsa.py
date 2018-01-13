# coding:utf-8
# python 2.7
import random
# (a ** n) % m
def quickPowMod(a, n, m):
	ans = 1
	while n:
		if n & 1:
			ans = ans * a % m
		a = a * a % m
		n >>= 1
	return ans

def miller_rabin(n):
	if n & 1 == 0:
		return False
	a = n - 1
	s = 0
	while 1:
		if a % 2 == 0:
			s += 1
			a = a / 2
		else: break
	t = int(a)
	# print s, t
	
	for i in range(5):
		b = random.randint(2, n - 2)
		r0 = quickPowMod(b, t, n)
		if r0 == 1 or r0 == n - 1:
			continue
		elif r0 != 1 and r0 != n - 1:
			ri = r0
			for i in range(s):
				ri = quickPowMod(ri, 2, n)
				if ri == n - 1:
					break
				elif ri != n - 1 and i == s - 1:
					return False
				elif ri != n - 1:
					continue
	return True

def get_big_pri():
	num = num_gen(127)
	flag = miller_rabin(num)
	while flag == False:
		num += 2
		flag = miller_rabin(num)
	return num

def gcd(a, b):
	if a < b:
		a, b = b, a
	while b != 0:
		temp = a % b
		a = b
		b = temp
	return a

def extend_euclid(a, b, x, y):
    if b == 0:
        return a,1,0
    r,t,y = extend_euclid(b, a % b, x, y)
    x,y = y,t - a / b * y
    return r,x,y

# 随机生成一定二进制长度的整数
def num_gen(length):
	temp = ''
	for i in range(length):
		temp += str(random.randint(0,1))
	temp += '1'
	return int(temp, 2)

def key_gen():
	# 生成两个大素数
	p = get_big_pri()
	q = get_big_pri()
	# 乘积
	n = p * q
	# fai（n）
	euler_n = (p - 1) * (q - 1)
	# 随机找出一个e
	while True:
		e = random.randint(7, euler_n)
		if miller_rabin(e) == True and gcd(e, euler_n) == 1:
			break
		else: continue
	# 计算d
	x = y = 0
	d = extend_euclid(euler_n, e, 1, 0)[2]
	if d < 0: d = d + euler_n
	if e > d: e,d = d,e
	# print 'p =', p, 'q =', q
	# print 'n =', n
	# print 'euler_n =', euler_n
	# print 'e =', e
	# print 'd =', d
	return e,d,n

if __name__ == '__main__':
	e,d,n = key_gen()
	print '公钥：', e,n
	print '私钥：', d,n
	plain = 78900128937812978912739812
	cipher = quickPowMod(plain, e, n)
	print cipher
	plain2 = quickPowMod(cipher, d, n)
	print plain2

	

