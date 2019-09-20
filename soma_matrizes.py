#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Construa um programa que efetue a soma de duas matrizes.
# • Regras
# – Para adicionarmos duas ou mais matrizes é preciso que todas elas tenham o mesmo número de linhas e de colunas.
# – A soma das matrizes irá resulta em outra matriz que também terá o mesmo número de linhas e de colunas.
# – Os termos deverão ser somados com os seus termos correspondentes.
# • O usuário deverá fornecer todos os elementos das matrizes a serem somadas.
# • O atendimento das regras para a soma das matrizes deverá ser implantado pelo programa.
# • O programa deverá apresentar as matrizes a serem somadas e a matriz resultado da soma.
# matriz = [[a11, a12, a13], [b11, b12, b13], [c11, c12, c13]]
matriz_linha = []
matriz_coluna = []
matriz1 = []
matriz2 = []
soma_matrizes = []
ct = 0
ctm = 0
ctn = 0
m = int(raw_input("Número de linhas da matriz: "))
n = int(raw_input("Número de colunas da matriz: "))
qtde_elementos = m * n
if m != n:
	print "É preciso que todas as matrizes tenham o mesmo número de linhas e de colunas."
else:
	print "Tipo da matriz:", m, "x", n
	for i in range(qtde_elementos):
		ctm = ct + 1
		for i in range(m):
			ctn = ctn + 1
			elemento = float(raw_input("Linha %d, Coluna %d: " % (ct, ctn)))
