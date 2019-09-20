#!/usr/bin/env python
# -*- coding: utf-8 -*-
# • Considere as seguintes regras para a definição do valor do imposto de renda:
# – Rendimento anual (R$)
# • 0,00 a 24.000,00 – isento de tributação • 24.001,00 a 72.000,00 – alíquota de 15%
# • Acima de 72.000,00 – alíquota de 25%
# – Deduções (R$): • Saúde: 6.000,00 • Dependentes: 1.200,00 por dependente (máximo de R$ 6.000,00)
# • O valor do imposto devido será calculado sobre o valor do rendimento anual considerando o montante das deduções. • Se, ao final do cálculo, o valor do imposto devido for negativo, o programa deverá informar “Valor do imposto a restituir = R$ ...”
aliquota = 0
rend_anual = 0
imposto_devido = 0
ded_saude = 0
ded_dep = 0
rend_anual = float(raw_input("Rendimento anual: "))
qtde_dep = int(raw_input("Quantidade de dependentes: "))
ded_saude = float(raw_input("Gastos anuais com saúde: "))
ded_dep = 1200 * qtde_dep
if rend_anual > 0 and rend_anual <= 24000: print "Isento de imposto de renda"
else:
	if rend_anual > 24000 and rend_anual <= 72000: aliquota = 0.15
	else: aliquota = 0.25
	print "Alíquota de", aliquota * 100, "%"
if ded_saude > 6000:
	ded_saude = 6000
if ded_dep > 6000:
	ded_dep = 6000
ded_ir = rend_anual * aliquota
montante_deducoes = ded_ir + ded_dep + ded_saude
imposto_devido = rend_anual - montante_deducoes
if imposto_devido < 0:
	print "Valor do imposto a restituir: R$", ded_ir - imposto_devido
print 
print "Renda anual: R$", rend_anual
print "Gastos por dependente: R$ 1200,00"
print "Quantidade de dependentes: ", qtde_dep
print "Gastos totais com dependentes: R$", ded_dep
print "Gastos com saúde: R$", ded_saude
