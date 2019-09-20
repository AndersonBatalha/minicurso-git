#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Cada 20 kg acima do peso de 150 kg, implica em uma redução de autonomia de 2 %. O usuário deverá fornecer a quantidade de ocupantes e o peso de cada um deles.
distancia = float(raw_input("Distância a ser percorrida em km: "))
vmedia = float(raw_input("Velocidade média: "))
etanol = float(raw_input("Quantidade em litros de etanol: "))
gasolina = float(raw_input("Quantidade em litros de gasolina: "))
vtotal = etanol + gasolina
ocupantes = int(raw_input("Quantidade de ocupantes: "))
peso_total = []
for i in range(ocupantes):
	peso = float(input("Peso do passageiro: "))
	peso_total.append(peso)
	soma = sum(peso_total)
	if peso_total >= 150:
		excesso = (soma - 150) / 20
		reducao_peso = excesso * 0.2
	else: print "O peso total dos ocupantes não ultrapassou o limite de 150 kg."
print "A soma do peso de todos os ocupantes: ", soma, "kg."
print "Redução de autonomia com o peso excedente dos passageiros:", reducao_peso

if etanol == 0:
	print "100 % de gasolina."
	rend_gasolina = 22 * gasolina
	print "Autonomia de", rend_gasolina, "litros de gasolina."
	if vmedia > 0 and vmedia <= 80: reducao = rend_gasolina * 0.2
	else: reducao = rend_gasolina * 0.3
	novo_rend_gasolina = rend_gasolina - (reducao + reducao_peso)
	if distancia > rend_etanol: print "Serão necessários", distancia -rend_etanol, "litros de etanol para completar a viagem."
if gasolina == 0:
	print "100 % de etanol."
	rend_etanol = 15 * etanol
	print "Autonomia de", rend_etanol, "litros de etanol."
	if vmedia > 0 and vmedia <= 80: reducao = rend_etanol * 0.2
	else: reducao = rend_etanol * 0.3
	novo_rend_etanol = rend_etanol - (reducao + reducao_peso)
	if distancia > rend_gasolina: print "Serão necessários", distancia - rend_gasolina, "litros de gasolina para completar a viagem."
if gasolina > 0 and etanol > 0:
	print "Mistura de etanol e gasolina."
	perc_gasolina = gasolina / vtotal
	perc_etanol = etanol / vtotal
	print "Percentual de gasolina:", int(perc_gasolina * 100), "%"
	print "Percentual de etanol:", int(perc_etanol * 100), "%"
	if perc_etanol > 0 and perc_etanol <= 0.10: rend_misto = 21 * etanol
	elif perc_etanol > 0.10 and perc_etanol <= 0.20: rend_misto = 20 * etanol
	elif perc_etanol > 0.20 and perc_etanol <= 0.30: rend_misto = 19 * etanol
	elif perc_etanol > 0.30 and perc_etanol <= 0.40: rend_misto = 18 * etanol
	elif perc_etanol > 0.40 and perc_etanol <= 0.50: rend_misto = 17 * etanol
	else: rend_misto = 16 * etanol
	print "O rendimento com etanol e gasolina foi de", rend_misto, "litros."
	if rend_misto > distancia:
		print "O carro abastecido faz", rend_misto - reducao_peso, "quilômetros com", vtotal, "litros a mistura de etanol e gasolina. Sobrarão", rend_misto - distancia, "litros de gasolina no tanque."
	else:
		saldo = distancia - rend_misto
		print "Distância a percorrer: %d km" % saldo
		gas = saldo / 22
		eta = saldo / 15
		tempo = rend_misto / vmedia
		print "Dentro de %d horas, o veículo precisará de %d litros de gasolina ou %d litros de etanol (considerando a velocidade média de 80 km/h)" % (tempo, gas, eta)
