#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Arquivos

print("""
=============================================================
Python - Acesso a arquivos
=============================================================
""")

arq = open("arquivo.txt", "w")
for i in range(1, 101):
	arq.write("%da Linha\n" % i)
arq.close()

npares = open("pares.txt", "w")
nimpares = open("impares.txt", "w")
npares.write("Números pares de 1 a 100:\n")
nimpares.write("Números ímpares de 1 a 100:\n")
for i in range(0, 101):
	if i % 2 == 0:
		npares.write("%d\n" % i)
	else:
		nimpares.write("%d\n" % i)
npares.close()
nimpares.close()

maior_venda = 0
arquivo = open("vendas.txt")
for linha in arquivo:
	(nome, vendas, cidade) = linha.split(";")
	if float(vendas) > maior_venda:
		maior_venda = float(vendas)
arquivo.close()
print "A maior venda foi a %s" % vendas
maiorvenda=0
resultado = open("vendas.txt")
for linha in resultado:
	(nome, venda, cidade) = linha.split(";")
	if float(venda) > maiorvenda:
		maiorvenda = float(venda)
resultado.close()
print "A maior venda foi de %5.2f" % maiorvenda
