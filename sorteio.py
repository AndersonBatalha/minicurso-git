#!/usr/bin/env python
# -*- coding: utf-8 -*-
nome = cpf = endereco = bairro = cidade = estado = " "
dados_pessoais = []
possiveis_premios = []
sorteio = {}
opcao = 0
l = ["1 - Nome", "2 - CPF", "3 - Endereço", "4 - Bairro", "5 - Cidade"]
import random
class Dados:
	def __init__(self, nome, cpf, endereco, bairro, cidade, estado):
		self.nome = nome
		self.cpf = cpf
		self.endereco = endereco
		self.bairro = bairro
		self.cidade = cidade
		self.estado = estado
	def descricao(self):
		print """O código abaixo faz um sorteio de um prêmio qualquer. No início do programa, o usuário tem a opção de sair do programa ou pode fazer o cadastro de participantes. No cadastro, o usuário define o número de participantes do sorteio. Esses participantes recebem um número aleatório (de 1 a 1.000.000) e podem ver seus dados individualmente ou de todos. Também pode ser feito a alteração ou a exclusão de dados através do número aleatório recebido anteriormente."""
	def sair(self):
		print "1 - Sair."
	def cadastro(self):
		n = int(input("Número de participantes: "))
		print "Cadastre seus dados pessoais para participar:"
		for i in range(n):
			numero = random.randint(1, 1000000)
			nome = raw_input("Nome: ")
			cpf = raw_input("CPF: ")
			endereco = raw_input("Endereço: ")
			bairro = raw_input("Bairro: ")
			cidade = raw_input("Cidade: ")
			estado = raw_input("Estado: ")
			identificacao = Dados(nome, cpf, endereco, bairro, cidade, estado)
			print
			dados_pessoais = [identificacao.nome, identificacao.cpf, identificacao.endereco, identificacao.bairro, identificacao.cidade, identificacao.estado]
			sorteio[numero] = dados_pessoais
			if len(identificacao.nome) == 0 or len(identificacao.cpf) == 0 or len(identificacao.endereco) == 0 or len(identificacao.bairro) == 0 or len(identificacao.cidade) == 0 or len(identificacao.estado) == 0:
				print "Algum dos campos não foi preenchido. Tente novamente."
	def individual(self):
		print "Opção 1 - Individual"
		print "Números disponíveis:"
		for i in range(len(sorteio.keys())):
			print sorteio.keys()[i]
		opcao = int(raw_input("Digite o número a ser visualizado: "))
		while opcao not in sorteio.keys():
			print "Número não existe!"
			opcao = int(raw_input("Digite o número a ser visualizado: "))
		else:
			if opcao in sorteio.keys():
				print "Nome:", sorteio[opcao][0]
				print "CPF:", sorteio[opcao][1]
				print "Endereço:", sorteio[opcao][2]
				print "Bairro:", sorteio[opcao][3]
				print "Cidade:", sorteio[opcao][4],"(", sorteio[opcao][5],")"
	def todos_os_participantes(self):
		print "Opção 2 - Todos os participantes"
		for numero, dados_pessoais in sorteio.items():
			print "Seu número:", numero
			print "Nome:", dados_pessoais[0]
			print "CPF:", dados_pessoais[1]
			print "Endereço:", dados_pessoais[2]
			print "Bairro:", dados_pessoais[3]
			print "Cidade:", dados_pessoais[4], "(", dados_pessoais[5],")"
			print
	def altera_dados(self):
		print "3 - Alteração de dados.\nNúmeros disponíveis:"
		for i in range(len(sorteio.keys())):
			print sorteio.keys()[i]
		opcao = int(raw_input("Digite o número a ser alterado: "))
		while opcao not in sorteio.keys():
			print "Número não existe!"
			opcao = int(raw_input("Digite o número a ser alterado: "))
		else:
			for numero, dados_pessoais in sorteio.items():
				if opcao in sorteio.keys():
					print "O número existe.\nEscolha o item a ser alterado:\n1 - Nome / 2 - CPF / 3 - Endereço / 4 - Bairro / 5 - Cidade"
					opcao1 = int(raw_input("Opção: "))
					if opcao1 == 1:
						novo_item = raw_input("Digite o novo Nome: ")
					elif opcao1 == 2:
						novo_item = raw_input("Digite o novo CPF: ")
					elif opcao1 == 3:
						novo_item = raw_input("Digite o novo Endereço: ")
					elif opcao1 == 4:
						novo_item = raw_input("Digite o novo Bairro: ")
					elif opcao1 == 5:
						novo_item = raw_input("Digite a nova Cidade: ")
					sorteio[opcao][opcao1 - 1] = novo_item
					print "Com a Alteração:"
					if opcao in sorteio.keys():
						print "Nome:", sorteio[opcao][0]
						print "CPF:", sorteio[opcao][1]
						print "Endereço:", sorteio[opcao][2]
						print "Bairro:", sorteio[opcao][3]
						print "Cidade:", sorteio[opcao][4],"(", sorteio[opcao][5],")"
	def exclui_dados(self):
		print "4 - Exclusão de dados.\nExistem os seguintes números disponíveis:"
		for i in range(len(sorteio.keys())):
			print sorteio.keys()[i]
		opcao = int(raw_input("Digite o número a ser excluído: "))
		while opcao not in sorteio.keys():
			print "Número não existe!"
			opcao = int(raw_input("Digite o número a ser excluído: "))
		else:
			for numero, dados_pessoais in sorteio.items():
				if opcao in sorteio.keys():
					del sorteio[opcao]
					print "Registro %s excluído." % opcao
					print sorteio
	def fazer_sorteio(self):
		print "5 - Fazer o sorteio e exibir o ganhador.\nNúmeros disponíveis:"
		for i in range(len(sorteio.keys())):
			print sorteio.keys()[i]
		print "Número vencedor:", random.choice(sorteio.keys())
		print "Nome:", sorteio[random.choice(sorteio.keys())][0]
		print "CPF:", sorteio[random.choice(sorteio.keys())][1]
		print "Endereço:", sorteio[random.choice(sorteio.keys())][2]
		print "Bairro:", sorteio[random.choice(sorteio.keys())][3]
		print "Cidade:", sorteio[random.choice(sorteio.keys())][4],"(", sorteio[random.choice(sorteio.keys())][5],")"
		possiveis_premios = ["Torradeira", "Jogo de Panelas", "Carro 0 km", "R$ 500.000", "Casa própria", "Luminária", "Televisão", "Geladeira"]
		print "Você pode ganhar:"
		for i in range(len(possiveis_premios)):
			print possiveis_premios[i]
		print "Você ganhou: %s" % (random.choice(possiveis_premios))
arquivo = open("log.txt", "w")
for i in range(len(l)):
	arquivo.write("%s\n" % l[i])
arquivo.close()
