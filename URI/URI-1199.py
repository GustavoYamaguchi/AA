n = raw_input()

while n != "-1":
	if((len(n) > 1) and (n[1] == "x")):
		print (int(n, 16))
	else:
		result = ("0x" + str.upper(hex(int(n))[2:]))
		print result
	n = raw_input()