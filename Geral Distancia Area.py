#!/usr/bin/env python
# -*- coding: utf-8 -*-
import distanciaarea   # importa o modulo distanciaarea.py
def valida_inteiro(valor):  # define uma funcao para validar a entrada de dados, note que esta função é recursiva
    while True:
        try:
            a = int(valor)
            return a
            break
        except:
            print("O valor deve ser inteiro!")
            valor = valida_inteiro(input("Digite o novo valor: "))
# Solicita a entrada de dados, de cada uma das coordenadas dos pontos 1 e 2.
# Utiliza a função valida_inteiro definida anteriormente para validar a entrada de cada item de dados
x1 = valida_inteiro(input("Digite o valor da coordenada X do ponto 1: "))
y1 = valida_inteiro(input("Digite o valor da coordenada Y do ponto 1: "))
x2 = valida_inteiro(input("Digite o valor da coordenada X do ponto 2: "))
y2 = valida_inteiro(input("Digite o valor da coordenada Y do ponto 2: "))
# atribui para a variável distancia o resultado da execução da função distancia definida no módulo distanciarea.py
distancia = distanciaarea.distancia(x1,y1,x2,y2)
print("A distancia entre os pontos 1 e 2 é de %4.2f" % distancia)
opcao = input("Os pontos 1 e 2 formam as extremidades de um lado de um quadrado? (S/N): ")
if opcao=="S":
    area = distanciaarea.areaquadrado(x1,y1,x2,y2) # atribui para a variável area o resultado da execução da função areaquadrado definida no módulo distanciarea.py
    print("A área do quadrado cujo lado é delimitado pelos pontos 1 e 2 é %4.2f" % area)
