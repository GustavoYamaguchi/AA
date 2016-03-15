n = int(raw_input())

for i in range(n):
	s = raw_input()
	q = int(raw_input())
	for j in range(q):
		result = "Yes"
		r = raw_input()
		index = 0
		for k in r:
			index = s.find(k, index) + 1
			if index <= 0:
				result = "No"
				break
		print result