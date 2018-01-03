#coding:utf-8
import random
with open("dec.txt", "w") as f:
	for i in range(1024*10):
		a = chr(random.randint(0,127))
		f.write(a)