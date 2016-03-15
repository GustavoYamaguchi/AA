# -*- coding: utf-8 -*-

linha1 = raw_input()
linha2 = raw_input()
numero1 = ""
numero2 = ""

pontos = 0
decimais = 0
ponto = False

for i in linha1:
	if(i == "."):
		numero1 += "."
		ponto = True
	if i.isdigit():
		if(ponto):
			decimais += 1
			if decimais >2:
				break
		numero1 += i

pontos = 0
decimais = 0
ponto = False

for i in linha2:
	if(i == "."):
		numero2 += "."
		ponto = True
	if i.isdigit():
		if(ponto):
			decimais += 1
			if decimais > 2:
				break
		numero2 += i

print "cpf %s" % numero1[:11]
print "%.2f" % (float(numero1[11:]) + float(numero2))