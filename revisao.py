#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Estruturas de repetição:
print "Enquanto x for maior ou igual a 5, essa condição se repete: "
x = 0
while x <= 5:
	x = x + 1
	print x
print
print "Digite um número para somar ou 0 para sair"
s = 0
while True:
	v = int(raw_input(": "))
	if v == 0: break
	else:
		s = s + v
print "Soma: %d" % s
print
print "Tabuada"
tabuada = 1
while tabuada <= 10:
	numero = 1
	while numero <= 10:
		numero += 1
		print "%2.0d x %2.0d = %4.0d" % (tabuada, numero, tabuada * numero)
	tabuada += 1
