# -*- coding: utf-8 -*-

# 2 -> 5
# 3 -> 14
# 8 -> 204

n = int(raw_input())
while n != 0:
	soma = 0

	for i in range(1,n+1):
		soma += i**2

	print soma
	n = int(raw_input())