import math
tamanho = 1000002
primos = [True] * (tamanho+1)
primos[0] = False
primos[1] = False

for i in range(2, int(math.sqrt(tamanho))+1):
	if(primos[i]):
		for j in range(i*i, tamanho, i):
			primos[j] = False

somaDosPrimosGemeos = [0] * (tamanho+1)
for i in range(1, tamanho):
	if(primos[i] and (primos[i-2] or primos[i+2])):
		somaDosPrimosGemeos[i] = somaDosPrimosGemeos[i-1] + 1
	else: somaDosPrimosGemeos[i] = somaDosPrimosGemeos[i-1]

for i in range(int(raw_input())):
	n, m =map(int, raw_input().split())
	if n>m:
		n_temp = m
		m = n
		n = n_temp
	print somaDosPrimosGemeos[m] - somaDosPrimosGemeos[n-1]