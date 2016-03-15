dic = {}
mortos = set()

while True:
	try:
		assassino, assassinado = raw_input().split()
		mortos.add(assassinado)
		if(assassino in dic):
			dic[assassino] += 1
		else:
			dic[assassino] = 1
	except(EOFError):
		break

assassinos = dic.keys()
assassinos.sort()

print "HALL OF MURDERERS"
for i in assassinos:
	if(i not in mortos):
		print i, dic[i]