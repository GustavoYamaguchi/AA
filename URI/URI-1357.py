quantidadeDeNumeros = int(raw_input())
dict = {("*..."):1, ("*.*."):2, ("**.."):3, ("**.*"):4, ("*..*"):5, ("***."):6, ("****"):7, ("*.**"):8, (".**."):9,(".***"):0}

def primeiraLinhaPorNumero(i):
	linha = ""
	if(i == 0) or (i == 9):
		linha += "."
	else:
		linha += "*"
	if (i == 1) or (i == 2) or (i == 5) or (i == 8):
		linha += "."
	else:
		print i
		linha += "*"
	return linha

def segundaLinhaPorNumero(i):
	linha = ""
	if (i != 2) and(i >= 1) and (i <= 5):
		linha += "."
	else:
		linha += "*"
	if (i == 1) or (i == 2) or (i == 3) or (i == 6) or (i == 9):
		linha += "."
	else:
		linha += "*"
	return linha


while quantidadeDeNumeros != 0:
	tipoDeTraducao = raw_input()
	mensagem = raw_input()
	if tipoDeTraducao=="S":
		mensagem = map(int, list(mensagem))
		primeiraLinha = ""
		segundaLinha = ""
		terceiraLinha = ""
		for numero in mensagem:
			primeiraLinha += primeiraLinhaPorNumero(numero) + " "
			segundaLinha += segundaLinhaPorNumero(numero) + " "
			terceiraLinha += ".. "
		print primeiraLinha[:-1]
		print segundaLinha[:-1]
		print terceiraLinha[:-1]
	elif tipoDeTraducao=="B":
		mensagem = mensagem.split()
		mensagem2 = raw_input().split()
		mensagem3 = raw_input()
		resp = ""
		for i in range(len(mensagem)):
			resp += str(dict[mensagem[i] + mensagem2[i]])
		print resp
	quantidadeDeNumeros = int(raw_input())