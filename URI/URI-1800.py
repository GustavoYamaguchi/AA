n = int(raw_input().split()[0])
escritoriosVisitados = set().union(map(int, raw_input().split()))

for i in range(n):
	escritorio = int(raw_input())
	if escritorio in escritoriosVisitados:
		print 0
	else:
		escritoriosVisitados.add(escritorio)
		print 1