#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Questão da prova - cadastro de alunos.
nfaltas = 0
nota = 0
dados_alunos = {}
notas = []
frequencia = []
import random
while True:
	opcao = raw_input("Deseja adicionar dados dos alunos? ")
	if opcao == "s" or opcao == "S":
		matricula = random.randint(1, 1000000)
		for i in range(4):
			nota = float(raw_input("Nota: "))
			nfaltas = float(raw_input("Número de faltas: "))
			notas.append(nota)
			frequencia.append(nfaltas)
		print """Digite: 1 - Alterar / 2 - Remover"""
	elif opcao == "n" or opcao == "N":
		print "Encerrado"
		break
	else: print "Digite apenas S ou N."
print dados_alunos
