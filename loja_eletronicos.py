#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Considere a existência de uma loja de produtos eletrônicos. Esta loja possui uma série de produtos que possuem caracteristicas comuns. Por exemplo: o equipamento tv pode possuir o atributo tela lcd (false ou true). Da mesma forma, este equipamento pode possuir uma série de outros atributos distintos de outros produtos. A mesma loja possui um cadastro de clientes, cada um deles com características pró́prias, e que, també́m podem ser compartilhadas por uma sé́rie de clientes. Esta loja pode executar operaçõ̃es comerciais como por exemplo: venda e devoluçã̃o de produtos. Fazendo uso dos conceitos de funçõ̃es, listas, dicioná́rios, classes, objetos e módulos, construa a codificaçã̃o necessá́ria para abordar todo o ambiente descrito anteriormente.
polegadas = estoque = operacao = 0
marcas = []
cadastro = {}
def cadastro(polegadas, estoque):
	print "1 - Sim\n2 - Não"
	opcao = int(raw_input("Fazer o cadastro? "))
	if opcao == 1:
		nome = raw_input("Nome: ")
		cpf = raw_input("CPF: ")
		endereco = raw_input("Endereço: ")
		bairro = raw_input("Bairro: ")
		cidade = raw_input("Cidade: ")
		estado = raw_input("Estado: ")
	print "1 - Venda\t2 - Devolução"
	operacao = int(raw_input("Operação: "))
	if operacao == 1:
		estoque = int(raw_input("Itens no estoque: "))
		print "Venda\n1 - LCD\t2 - LED\nExistem %d televisores no estoque." % estoque
		tipo = int(raw_input("Tipo: "))
		polegadas = int(raw_input("Polegadas: "))
		marcas = ["LG", "Panasonic", "Gradiente", "Samsung", "Hitachi", "Toshiba", "AOC"]
		for i in range(len(marcas)):
			print i + 1, "-", marcas[i]
		marca = int(raw_input("Marca: "))
		print "Televisor de %d polegadas da marca %s" % (polegadas, marcas[marca - 1])
		estoque -= 1
	elif operacao == 2:
		print "Devolução"
		estoque += 1
		print "Existem %d televisores no estoque." % estoque
	else:
		print "Inválido."
print cadastro(polegadas, estoque)
