k = int(raw_input())

while k!= 0:
	n,m = map(int, raw_input().split())
	for i in range(k):
		x,y = map(int, raw_input().split())
		if (x == n or y == m):
			print "divisa"
		else:
			result = ""
			if(y > m):
				result += "N"
			else:
				result += "S"
			if(x > n):
				result += "E"
			else:
				result += "O"
			print result
	k = int(raw_input())
