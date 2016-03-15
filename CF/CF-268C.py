coordenadas = map(int, raw_input().split())
pontos = min(coordenadas[0], coordenadas[1]) + 1

print pontos

for i in range(pontos):
	print i,pontos-i-1