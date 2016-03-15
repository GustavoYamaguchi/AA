while True:
	try:
		parenteses = ""
		result = ""
		for i in raw_input():
			if i =="(":
				parenteses += "("
			if i == ")":
				if "(" in parenteses:
					parenteses = parenteses[:len(parenteses)-1]
				else:
					result = "incorrect"
		if result != "incorrect" and parenteses == "":
			print "correct"
		else: print "incorrect"
	except(EOFError):
		break