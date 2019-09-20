#!/usr/bin/env python
# -*- coding: utf-8 -*-
class seguranca_residencial:
	def __init__ (self):
		self.sensor_ligado = False
		self.sensor_desligado = False
		self.captura_imagem = False
		self.monitora_ambiente = False
		self.envia_alerta = False
		self.tipo = ""
		self.opcao = 0
	def operacoes(self):
		opcao = raw_input("Ligar os sensores e iniciar monitoramento? ")
		if self.opcao == "S" or self.opcao == "s":
			self.sensor_ligado = True
			self.monitora_ambiente = True
			print "Sensores ligados."
			print
			print "1 - Solicitar captura de imagem\t2 - Enviar alerta"
			tipo = int(raw_input("Escolha uma das opções acima: "))
			if self.tipo == 1:
				self.captura_imagem = True
				print "Imagem capturada."
			elif self.tipo == 2:
				self.envia_alerta = True
				print "Alerta enviado."
			else:
				print "Informe apenas 1 ou 2!"
		elif self.opcao == "N" or self.opcao == "n":
			self.sensor_desligado = True
			print "Sensores desligados."
		else:
			print "Informe apenas S ou N!"
