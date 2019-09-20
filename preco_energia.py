#!/usr/bin/env python
# -*- coding: utf-8 -*-
# • Escreva um programa que calcule o preço a pagar pela energia elétrica. Pergunte a quantidade de kWh consumidas e o tipo de instalação:
# Residências: R / Indústrias: I / Comércios: C
# • A tabela ao lado deverá ser utilizada para o cálculo do preço da energia:
#	 Preço por tipo e faixa de consumo
#	 Tipo			kWh					Preço
# Residencial		Até 500				R$ 0,40
#					Acima de 500		R$ 0,65
# Comercial			Até 1000			R$ 0,55
#					Acima de 1000		R$ 0,60
# Industrial		Até 5000			R$ 0,55
#					Acima de 500		R$ 0,60
print """Cálculo do preço da energia elétrica. Informe o tipo da
instalação com letras maiúsculas ou minúsculas:
R - Residencial / C - Comércio / I - Indústria """
tipo = raw_input("Informe o tipo da instalação: ")
consumo_kwh = float(raw_input("Consumo de kWh: "))
if tipo != "R" and tipo != "r" and tipo != "I" and tipo != "i" and tipo != "C" and tipo != "c": print "Informe letra válida. Tente novamente!"
else:
	if tipo == "R" or tipo == "r":
		print "Tipo de instalação: Residencial"
		if consumo_kwh < 500: total = consumo_kwh * 0.4
		else: total = consumo_kwh * 0.65
	elif tipo == "C" or tipo == "c":
		print "Tipo de instalação: Comércio"
		if consumo_kwh < 1000: total = consumo_kwh * 0.55
		else: total = consumo_kwh * 0.6
	else:
		print "Tipo de instalação: Industrial"
		if consumo_kwh < 5000: total =  consumo_kwh * 0.55
		else: total = consumo_kwh * 0.6
	print "Valor total da conta: R$", total
