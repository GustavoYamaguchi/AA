n = int(raw_input())
for iteracao in range(n):
	c,d = map(int,raw_input().split())
	if(c == d == 0):
		print 0
		continue
	print (26**c) * (10**d)