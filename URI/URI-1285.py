nums = map(int, raw_input().split())

# Analisar casos extremos, nos casos intermediarios: apenas adicionar a regra de numeros repetidos.
# Ex: Cada dezena, uma unidade sera ignorada. Cada centena, uma dezena sera ignorada, adicionada a regra das dezenas.

numInicial = nums[0]
numMeta = nums[1]
numIndice = numInicial
contador = 0

def existeNumerosIguais(n):
	splittedNum = map(int, str(n))
	for i in range(len(splittedNum)):
		for j in range(i+1,len(splittedNum)):
			if splittedNum[i] == splittedNum[j]:
				return True
	return False

def contaNumerosDiferentes():
	global contador
	global numIndice
	while numIndice <= numMeta:
		if(not existeNumerosIguais(numIndice)):
			contador = contador+1
		numIndice = numIndice+1
	return

contaNumerosDiferentes()
print contador