#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Um pouco de conjuntos e dicionários:
alfabeto_repete = ["a", "b", "a", "a", "a", "b", "c", "c", "d", "d",
"c", "b"]
print set(alfabeto_repete) # Caracteres que não se repetem na lista "alfabeto_repete"
a = set("felicidade") # Todas as letras de "felicidade" que não se repetem.
b = set("cidade") # Todas as letras de "cidade" que não se repetem."
print "Conjunto A:", a
print "Conjunto B:", b
print "Pertence A e não em B:", a - b
print "Pertence a A e B:", a & b
print "A ou B:", a | b
print "Pertence a A ou B, mas não os dois:", a ^ b
conjunto = set("Anderson")
print conjunto
conjunto.add("Pontes Batalha") # Adiciona a expressão "Pontes Batalha" ao conjunto
print conjunto
conjunto.remove("Pontes Batalha") # Remove a expressão "Pontes Batalha" do conjunto
print conjunto
print
# Dicionários

tabela = {20000: "Anderson", 20001: "Marcia", 20002: "Roberto", 20003: "Albert Einstein", 20004: "Leonardo da Vinci", 20005: "Marco Polo", 20006: "Santos Dumont", 20007: "Vasco da Gama", 20008: "John Lennon", 20009: "Yoko Ono"}
print tabela
print tabela[20004] # Acesso a um elemento através da chave
tabela [20001] = "Pero Vaz de Caminha" # Alteração de um elemento
print tabela # Lista com a alteração
print 19999 in tabela # Verifica se o item está presente. Retorna TRUE ou FALSE.
print tabela.keys() # Chaves do dicionário
print tabela.values() # Valores do dicionário
chaves = list(tabela.keys()) # Transforma as chaves do dicionário em uma lista.
print chaves
valores = list(tabela.values())
print valores # Transforma os valores do dicionário em uma lista.
del tabela[20000] # Remove o item do dicionário
print tabela

# Parece um banco de dados, mas não é ...
notas = {13013: [7, 4, 6, 2], 13014: [0, 10, 9, 8], 13015: [4, 6, 7, 8], 13016: [6.5, 7.5, 8, 9.5], 13017: [10, 10, 9, 8], 13018: [9, 7, 8, 6]}
print notas[13013][3] # nome_da_lista[chave][posição da lista]
print notas.items() # Retorna o par chave, valor (tupla do dicionário)
for matricula, nota in notas.items():
	print "Número de matrícula do aluno:", matricula
	print "Nota 1:", nota[0]
	print "Nota 2:", nota[1]
	print "Nota 3:", nota[2]
	print "Nota 4:", nota[3]
	soma = nota[0] + nota[1] + nota[2] + nota[3]
	media = soma / 4
	print "Soma das notas: %d.\Média: %d" % (soma, media)
	if media >= 6: print "Aprovado"
	else: print "Reprovado"
