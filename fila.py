#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Construa um programa para o atendimento de uma fila em uma agência bancária.
# • O atendimento deverá respeitar a ordem de chamada, ou seja: o primeiro a chegar será o primeiro a sair.
# • O atendente terá as seguintes opções:
#	– Atender o cliente;
#	– Encerrar o atendimento (sair do programa);
#	– Incluir novo cliente na fila.
# • O programa deverá apresentar mensagem identificando o cliente atendido e, além disso, caso a fila tenha sido totalmente atendida deverá apresentar mensagem indicando esta situação.
clientes = 0
senha = 0
fila = []
while True:
	opcao = int(raw_input("\n1 - Atender o cliente\n2 - Encerrar o atendimento\n3 - Incluir novo cliente\n\nEscolha as opções acima para iniciar o atendimento: "))
	if opcao == 1:
		if len(fila) == 0: print "Fila vazia. Sem clientes para serem atendidos."
		else:
			print fila, "\nCliente está sendo atendido. Existem %d pessoas na fila." % (len(fila))
	elif opcao == 2:
		if len(fila) == 0: print "Fila vazia."
		else:
			fila.remove(fila[0])
			print fila, "\nAtendimento encerrado. Existem %d pessoas na fila." % (len(fila))
	elif opcao == 3:
		senha += 1
		fila.append(senha)
		if len(fila) == 0: print "Fila vazia"
		else: print fila, "\nCliente incluído. Existem %d pessoas na fila." % (len(fila))
	else: print "Consideradas apenas opções entre 1 e 3."
