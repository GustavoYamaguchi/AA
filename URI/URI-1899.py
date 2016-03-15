quantidadeDeParedes = int(raw_input())
possivelCoeficiente = []
coefAngA, coefAngB = 0, 0

for i in range(quantidadeDeParedes+1):
	parede = map(int, raw_input().split())
	distancia = parede[0]
	alturaA = parede[1]
	alturaB = parede[2]
	coefAngA = (float(alturaA))/distancia
	coefAngB = (float(alturaB))/distancia
	possivelCoeficiente.append([coefAngA, coefAngB])

possivel = True
for i in range(1, len(possivelCoeficiente)):
	if (possivelCoeficiente[i][0] > possivelCoeficiente[i-1][1]) or (possivelCoeficiente[i][1] < possivelCoeficiente[i-1][0]):
		possivel = False
		break
	else:
		if (possivelCoeficiente[i][0] < possivelCoeficiente[i-1][0]):
			possivelCoeficiente[i][0] = possivelCoeficiente[i-1][0]
		if (possivelCoeficiente[i][1] > possivelCoeficiente[i-1][1]):
			possivelCoeficiente[i][1] = possivelCoeficiente[i-1][1]

if possivel:
	print "Y"
else:
	print "N"