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

# 随机生成一定二进制长度的整数
def gen(length):
	temp = ''
	for i in range(length):
		temp += str(random.randint(0,1))
	return int(temp, 2)

if __name__ == '__main__':
	a = gen(64)
	n = gen(32)
	m = gen(128)
	print ('(', a, '**', n, ') %', m, '=', quickPowMod(a,n,m))
