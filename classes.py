#!/usr/bin/env python
# -*- coding: utf-8 -*-
nome = raw_input("Nome: ")
cpf = raw_input("CPF: ")
endereco = raw_input("Endereço: ")
bairro = raw_input("Bairro: ")
cidade = raw_input("Cidade: ")
estado = raw_input("Estado: ")
class informa_dados:
	def __init__ (self, nome, cpf, endereco, bairro, cidade, estado):
		self.nome = nome
		self.cpf = cpf
		self.endereco = endereco
		self.bairro = bairro
		self.cidade = cidade
		self.estado = estado
identificacao = informa_dados(nome, cpf, endereco, bairro, cidade, estado)
print "Eu, %s, portador do CPF %s, residente no endereço %s, bairro %s, cidade de %s (%s)."% (identificacao.nome, identificacao.cpf, identificacao.endereco, identificacao.bairro, identificacao.cidade, identificacao.estado)
