#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Adapte o programa do IR de modo a atender as seguintes condições:
# - O usuário deverá informar os gastos com saúde de forma individualizada, definindo a quantidade de itens e informando os valores de cada um deles.
# - O usuário poderá informar os dados dos dependentes de forma individual, apresentando os dados de cada um deles.
# Dependentes menores de 18 anos: dedução de R$ 1.200,00 para cada um deles.
# Dependentes maiores de 18 anos: dedução de R$ 900,00 para cada um deles.
aliquota = rend_anual = imposto_devido = ded_saude = ded_dep = 0
gastos_dep = []
gastos_saude = []
idades = []
nomes = []
rend_anual = float(raw_input("Rendimento anual: "))
qtde_dep = int(raw_input("Quantidade de dependentes: "))
for i in range(qtde_dep):
	nome = raw_input("Nome do dependente: ")
	idade_dependente = int(raw_input("Idade do dependente: "))
	nomes.append(nome)
	idades.append(idade_dependente)
	qtde_itens = int(raw_input("Quantidade de itens do dependente: "))
	print
	for i in range(qtde_itens):
		itens_saude = float(raw_input("Valor do gasto: R$ "))
	gastos_dep.append(ded_dep)
	gastos_saude.append(itens_saude)
for i in range(len(nomes)):
	print
	print "Dependente nº", i + 1
	print "Nome:", nomes[i]
	if idade_dependente > 18:
		ded_dep = 1200 * qtde_dep
		print "Maior de 18 anos. Dedução de R$ 1200,00"
	else:
		ded_dep = 900 * qtde_dep
		print "Menor de 18 anos. Dedução de R$ 900,00"
	print
if rend_anual > 0 and rend_anual <= 24000: print "Isento de imposto de renda"
else:
	if rend_anual > 24000 and rend_anual <= 72000: aliquota = 0.15
	else: aliquota = 0.25
	print "Alíquota de", aliquota * 100, "%"
ded_ir = rend_anual * aliquota
montante_deducoes = ded_ir + ded_dep + ded_saude
imposto_devido = rend_anual - montante_deducoes
if imposto_devido < 0: print "Valor do imposto a restituir: R$", ded_ir - imposto_devido
print "Renda anual: R$ %d\nQuantidade de dependentes: %d\nGastos com saúde: %d\nR$ Gastos com dependentes: %d\n", rend_anual, qtde_dep, sum(gastos_saude), sum(gastos_dep)
