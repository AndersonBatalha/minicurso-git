#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Uma cidade possui uma série de equipamentos digitais que medem e apresentam a temperatura e o horário local. Estes equipamentos estão espalhados por diversos pontos da cidade; No evento de uma temperatura superior a 28 graus e umidade inferior a 20%, estes equipamentos deverão mostrar alertas em suas telas; Além disso, devem permitir serem ligados ou desligados de forma remota e tambémtf permitir o ajuste da hora de cada um deles.
class cidade:
	def __init__(self):
		self.horario = horario
		self.temperatura = temperatura
		self.umidade = umidade
	def funcao(horario, temperatura):
		temperatura = int(raw_input("Informe a temperatura (em Celsius): "))
		horario = raw_input("Informe a hora local (No formato %h:%m): ")
		umidade = int(raw_input("Informe a umidade relativa do ar (em %):"))
		if temperatura > 28 and umidade < 20:
			print "Alta temperatura"
		else:
			pass
