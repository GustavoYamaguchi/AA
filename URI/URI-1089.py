# -*- coding: utf-8 -*-

n = int(raw_input())

while n != 0:
	magnitudes = map(int,raw_input().split())
	picos = 0
	sentido = ""
	for i in range(n+1):
		if i==0:
			if(magnitudes[-1] > magnitudes[0]):
				sentido = "decr"
			elif(magnitudes[-1] < magnitudes[0]):
				sentido = "cres"
		if i==n:
			if(magnitudes[-1] > magnitudes[0]) and sentido != "decr":
				picos += 1
				sentido = "decr"
			elif(magnitudes[-1] < magnitudes[0]) and sentido != "cres":
				picos += 1
				sentido = "cres"
		else:
			if(magnitudes[i-1] > magnitudes[i]) and sentido != "decr":
				picos += 1
				sentido = "decr"
			elif(magnitudes[i-1] < magnitudes[i]) and sentido != "cres":
				picos += 1
				sentido = "cres"
	print picos
	n = int(raw_input())