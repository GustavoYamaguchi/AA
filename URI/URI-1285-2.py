n = map(int, raw_input().split())
m = n[1]
n = n[0]
conjunto = set()
resposta = m-n+1

for numero in range(n,m+1):
	for digito in str(numero):
		if (digito in conjunto) and resposta > 0:
			resposta -= 1
		else:
			conjunto.add(digito)
	conjunto = set()

print resposta