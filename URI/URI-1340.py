while True:
	try:
		fila = []
		filaPrioridade = []
		pilha = []
		possivel = [True] * 3  # Fila, FilaPrioridade, Pilha
		for repeticao in range(int(raw_input())):
			n,m = map(int, raw_input().split())
			if n == 1:
				fila.append(m)
				filaPrioridade.append(m)
				filaPrioridade.sort(reverse=True)
				pilha.append(m)
			else:
				if(fila[0] == m and possivel[0]):
					del fila[0]
				else:
					possivel[0] = False
				if(filaPrioridade[0] == m and possivel[1]):
					del filaPrioridade[0]
				else:
					possivel[1] = False
				if(pilha[-1] == m and possivel[2]):
					del pilha[-1]
				else:
					possivel[2] = False
		if possivel.count(True) < 1:
			print "impossible"
		elif possivel.count(True) > 1:
			print "not sure"
		else:
			dataStructure = ["queue", "priority queue", "stack"]
			for i in range(len(possivel)):
				if possivel[i] == True:
					print dataStructure[i]
	except(EOFError):
		break