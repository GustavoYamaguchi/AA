t = int(raw_input())
chas = map(int, raw_input().split())

contador = 0
for i in chas:
	if i==t:
		contador +=1

print contador