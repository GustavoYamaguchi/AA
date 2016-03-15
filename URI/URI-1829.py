import math
n = int(raw_input())

results = [0,0] #lucas, pedro
rodadas = []
for i in range(1,n+1):
	a,b = map(int,raw_input().split("^"))
	fat = int(raw_input()[:-1])
	lucas = b*math.log10(a)
	pedro = 0
	for j in range(1,fat+1):
		pedro += math.log10(j)
	if lucas > pedro:
		results[0] += 1
		rodadas.append("Rodada #" + str(i) +": Lucas foi o vencedor")
	elif pedro > lucas:
		results[1] += 1
		rodadas.append("Rodada #" + str(i) +": Pedro foi o vencedor")

if(results[0] > results[1]):
	print "Campeao: Lucas!"
elif(results[1] > results[0]):
	print "Campeao: Pedro!"
else:
	print "A competicao terminou empatada!"

for i in rodadas:
	print i