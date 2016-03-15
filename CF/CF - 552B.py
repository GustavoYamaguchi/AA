n = raw_input()
n_size = len(n)
n = int(n)
result = 0

for i in range(1,n_size+1):
	if(i == n_size):
		result += (i * (n - (10**(i-1)) +1))
	else:
		m = int("1" + ("0" * (i-1)))
		result += 9* m * i

print result