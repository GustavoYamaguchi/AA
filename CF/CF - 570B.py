n, m = map(int, raw_input().split())

if((m-1) >  (n-m)):
	print m-1
elif ((n-m) > m-1):
	print m+1
else:
	if(n %2 != 0 and (n/2 + 1 == m)):
		if(n == m == 1):
			print n
		else:
			print m-1