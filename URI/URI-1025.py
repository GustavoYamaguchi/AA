n = raw_input()

contador = 1
 
def fazConsulta(marmores, numeroConsulta, comeco, fim):
	# 1 3 5 7 8 10 12
	if(numeroConsulta == marmores[comeco]):
		return comeco
	if((comeco == fim) and (numeroConsulta != marmores[comeco])):
		return -1
	meio = comeco + ((fim-comeco)/2)
	if numeroConsulta <= marmores[meio]:
		return fazConsulta(marmores, numeroConsulta, comeco, meio)
	else:
		return fazConsulta(marmores, numeroConsulta, meio+1, fim)
	return -1

while n != "0 0":
	print "CASE# %d:" % contador
	contador += 1
	q = int(n.split()[1])
	n = int(n.split()[0])
	marmores = []
	for i in range(n):
		marmores.append(int(raw_input()))
	marmores.sort()
	for i in range(q):
		numeroConsulta = int(raw_input())
		result = fazConsulta(marmores, numeroConsulta, 0, len(marmores)-1)
		if result >= 0:
			print numeroConsulta, "found at", result+1
		else:
			print numeroConsulta, "not found"
	n = raw_input()