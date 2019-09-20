#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Um pouco de listas
L = [] # Lista vazia
print "Lista vazia:", L
L = [10, 20, 30, 40] # Lista com 4 elementos
print "4 elementos:", L
L = range(10, 50, 10)
print "range(a, b, c) a -> início / b -> fim / c -> intervalo (c não é obrigatório) Ordem crescente."
print "Intervalo de 10 a 50:", L
print L[1], ": O acesso ao elemento através do índice."
L = range(40, -2, -2) 
print L, "Números pares de 0 a 40 em ordem decrescente"
print L[1:6], "Intervalo fechado a esquerda e aberto a direita."
print len(L), "Comprimento da lista"
print "a" in L, "Se um elemento pertence a lista. Retorna TRUE ou FALSE."
print "Números ímpares até 50."
for numero in range(50):
	if numero % 2 == 1:
		print numero,
# for
i = 0
while i < len(L):
	variavel = L[i]
	i += 1
	print variavel,
print
L1 = [10, 20, 30]
L2 = [40, 50, 60]
L3 = L1 + L2 
print L3, "Concatenação de listas"
print ["a", "b", "c", "d"] * 3, "Repetição de listas"
L1[2] = "Anderson", 
print L1, "Alteração de um elemento ocorre pelo índice. Lista com a alteração do elemento"
L2[0:3] = ["A", "P", "B", "Anderson Pontes Batalha"] 
print L2, "Alteração de vários elementos. Ocorre pelo intervalo"
L3[2:4] = [] 
print L3, "Remoção de elementos com uma lista vazia"
L1[1:1] = ["abc"] 
print L1, "Adição de elementos em fatia vazia"
L1.append(["Anderson", "Pontes", "Batalha"]) 
print L1, "append - acrescenta no final da lista"
L3.extend("c"), "Insere apenas um elemento de cada vez"
print L3
del(L1[0:1])
print L1, "remove elementos de uma lista"
L4 = ["a", "a", "a", "b", "c", 1, 2, 3]
print L4.index("a"), "Retorna a posição em que o elemento aparece."
print L4.count("a"), "Conta quantas vezes o elemento aparece na lista"
L4.sort()
print L4, "Embaralha os itens da lista"
L4.remove("a") 
print L4, "Remove o elemento"
L4.pop(1)
print L4
L5 = [1, 2, 3, 4, 5]
L5.reverse(), "Ordem inversa da lista"
print L5 
print "Usando listas como pilhas"
pilha = [3, 4, 5, 6]
pilha.append(7)
pilha.append(8)
pilha.append(9)
print pilha
print pilha.pop()
print pilha.pop()
print pilha.pop()
print pilha.pop()
print pilha.pop()
print pilha
a = "Anderson"
b = "Anderson"
print id(a), id(b), "id retorna a identificação do objeto"
L6 = [1, 2, 3]
L7 = [1, 2, 3]
print id(L6), id(L7), "Nas listas, o ID é diferente"
print "Listas aninhadas"
L8 = [1, 2, ["a", "b", "c"], 3, 4, 5]
print L8[2][1], "(L8[2][1]). Listas aninhadas. Uma lista dentro de outra."
