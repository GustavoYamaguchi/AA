n = int(raw_input())
numbers = map(int, raw_input().split())
somaAcumulada = [0]*n
somaAcumuladaReversa = [0]*n

for i in range(n):
	if i != 0:
		somaAcumulada[i] = numbers[i] + somaAcumulada[i-1]
		somaAcumuladaReversa[n-i-1] = numbers[n-i-1] + somaAcumuladaReversa[n-i]
	else:
		somaAcumulada[i] = numbers[i]
		somaAcumuladaReversa[n-i-1] = numbers[n-i-1]

resp = 0

for i in range(n-1):
	if somaAcumulada[i] == somaAcumuladaReversa[i+1]:
		resp +=1

print resp