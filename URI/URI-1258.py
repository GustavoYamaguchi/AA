n = int(raw_input())

while n!=0:
	brancoP = []
	brancoM = []
	brancoG = []
	vermelhoP = []
	vermelhoM = []
	vermelhoG = []
	for i in range(n):
		nome = raw_input()
		camisa = raw_input()
		if(camisa == "branco P"):
			brancoP.append(nome)
		elif(camisa == "branco M"):
			brancoM.append(nome)
		elif(camisa == "branco G"):
			brancoG.append(nome)
		elif(camisa == "vermelho P"):
			vermelhoP.append(nome)
		elif(camisa == "vermelho M"):
			vermelhoM.append(nome)
		elif(camisa == "vermelho G"):
			vermelhoG.append(nome)

	brancoP.sort()
	brancoM.sort()
	brancoG.sort()
	vermelhoP.sort()
	vermelhoM.sort()
	vermelhoG.sort()
	for i in brancoP:
		print "branco P", i
	for i in brancoM:
		print "branco M", i
	for i in brancoG:
		print "branco G", i
	for i in vermelhoP:
		print "vermelho P", i
	for i in vermelhoM:
		print "vermelho M", i
	for i in vermelhoG:
		print "vermelho G", i
	n = int(raw_input())
	if n !=0:
		print ""