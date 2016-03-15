casosDeTeste = int(raw_input())

for vezes in range(casosDeTeste):
	atingido = 0
	t = int(raw_input())
	alturas = map(int, raw_input().split())
	pulos = list(raw_input())

	for i in range(t):
		if((alturas[i] > 2) and (pulos[i]=="J")):
			atingido += 1
		elif((alturas[i] <= 2) and (pulos[i]=="S")):
			atingido +=1
	print atingido