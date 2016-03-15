n = int(raw_input())

dict = {}
keys = []

for i in range(n):
	old, new = raw_input().split()
	keys.append(old)
	dict[old] = new

result = []

def ultimoNomeDe(nome):
	global keys
	if(dict[nome] in keys):
		while (dict[nome] in keys):
			keys.remove(dict[nome])
			nome = dict[nome]
			if(dict[nome] not in keys):
				return dict[nome]
	else:
		return dict[nome]

for i in keys:
	result.append([i, ultimoNomeDe(i)])

print len(result)
for i in result:
	print i[0], i[1]