n = int(raw_input())
boysDS = map(int, raw_input().split())
m = int(raw_input())
girlsDS = map(int, raw_input().split())

boysDS.sort()
girlsDS.sort()

iBoys = 0
iGirls = 0
result = 0
while(iBoys < n and iGirls < m):
	if(abs(girlsDS[iGirls] - boysDS[iBoys]) <= 1):
		iBoys += 1
		iGirls += 1
		result += 1
	else:
		if boysDS[iBoys] > girlsDS[iGirls]:
			iGirls += 1
		else:
			iBoys += 1

print result