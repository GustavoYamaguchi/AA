import math
n = int(raw_input())

divisores = []
divisoresQuadrados = []
for i in range(2, int(math.sqrt(n)) +2):
	quadrado = i**2
	if(quadrado <= n and n % quadrado ==0):
		divisoresQuadrados.append(quadrado)
	if(n % i == 0):
		if i not in divisores:
			divisores.append(i)
		if n/i not in divisores:
			divisores.append(n/i)

divisores.append(n)
divisores.sort()
divisoresQuadrados.sort()

for i in divisores[::-1]:
	lovelyNumber = True
	for j in divisoresQuadrados:
		if i % j == 0:
			lovelyNumber = False
	if lovelyNumber:
		print i
		break