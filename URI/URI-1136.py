entrada1 = raw_input()
while entrada1 != "0 0":
	bolas = map(int, raw_input().split())
	quantidadeMeta = int(entrada1.split()[0])
	quantidadeDeBolas = int(entrada1.split()[1])

	numerosMeta = [False] * (quantidadeMeta+1)

	if 0 not in bolas:
		print "N"
		entrada1 = raw_input()
		continue

	for i in range(quantidadeDeBolas):
		for j in range(i, quantidadeDeBolas):
			numerosMeta[abs(bolas[i]-bolas[j])] = True

	if False not in numerosMeta:
		print "Y"
		entrada1 = raw_input()
		continue
	else:
		print "N"
		entrada1 = raw_input()
		continue