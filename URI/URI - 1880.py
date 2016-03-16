import string
digs = string.digits + string.letters

def int2base(x, base):
  if x < 0: sign = -1
  elif x == 0: return digs[0]
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)

def ehPalindromo(n):
  return str(n)==str(n)[::-1]

for i in range(int(raw_input())):
  bases = ""
  numero = int(raw_input())
  for j in range(2,17):
    if(ehPalindromo(int2base(numero,j))):
      bases += " %d" %(j)
  if bases != "":
    print bases[1:]
  else:
    print -1