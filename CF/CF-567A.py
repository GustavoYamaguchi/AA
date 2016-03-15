quantidade = int(raw_input())
distancias = map(int, (raw_input()).split())

for i in range(quantidade):
	if(i == 0):
		print "%d %d" % (abs(distancias[i] - distancias[1]), abs(distancias[i] - distancias[quantidade-1]))
	elif(i == quantidade-1):
		print "%d %d" % (abs(distancias[i] - distancias[i-1]), abs(distancias[i] - distancias[0]))
	else:
		print "%d %d" % (min(abs(distancias[i] - distancias[i-1]), abs(distancias[i] - distancias[i+1])),
						 max(abs(distancias[i] - distancias[0]), abs(distancias[i] - distancias[quantidade-1])))