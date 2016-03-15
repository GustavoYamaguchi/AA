while True:
	try:
		frase = raw_input()
		aux = ""
		result = ""
		flag = 0 # [0 : comeco - 1 : fim]
		for i in frase:
			if i == "[":
				if(flag== 0):
					result = aux + result
				else:
					result += aux
				aux = ""
				flag = 0
			elif i == "]":
				if(flag== 0):
					result = aux + result
				else:
					result += aux
				aux = ""
				flag = 1
			else:
				aux += i
		if(flag== 0):
			result = aux + result
		else:
			result += aux
		print result
	except(EOFError):
		break