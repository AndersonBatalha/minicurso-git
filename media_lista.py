#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Construa uma função para o cálculo da média de um conjunto de valores apresentados através de uma lista
n = 0
soma = 0
media_lista = 0
numero = 0
def media(n):
	n = int(raw_input("Número de elementos do conjunto: "))
	soma = 0
	lista = []
	for i in range(n):
		numero = int(raw_input("Número: "))
		lista.append(numero)
		soma = soma + numero
		media_lista = soma / n
	print lista, soma, media_lista
print media(n)
