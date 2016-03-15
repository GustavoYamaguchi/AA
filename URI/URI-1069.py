n = int(raw_input())
for iteracao in range(n):
	s = raw_input()
	contador = 0
	result = 0
	comeco = s.find("<")
	if (comeco >= 0):
		contador += 1
		for i in s[comeco+1:]:
			if(i == "<"):
				contador += 1
			elif(i == ">" and contador >0):
				contador -= 1
				result += 1
	print result