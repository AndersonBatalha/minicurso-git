#!/usr/bin/env python
# -*- coding: utf-8 -*-
equipes = [] # forma a lista de equipes vazia
jogos = []   # forma a lista de jogos vazia
while True:
    opcao = raw_input("Digite I para inclusão de equipe, T para montagem e apresentação da tabela de jogos e S para sair: ")
    if opcao == "S":
        break
    else:
        if opcao == "I":
            equipe = raw_input("Digite nome da equipe: ")
            equipes.append(equipe)
            print("%d equipes incluídas no campeonato" % len(equipes) )
        else:
            if opcao == "T":
                if len(equipes) < 2:
                    print("Não existem equipes suficientes para a montagem da tabela de jogos")
                else:
                    tamanho = len(equipes)
                    posicao = 0                 
                    while posicao < tamanho:
                        ct = 0
                        while ct < tamanho:
                            jogo = equipes[posicao] + " " + "x" + " " + equipes[ct]
                            if equipes[posicao] != equipes[ct]:
                                jogos.append(jogo)
                            ct = ct + 1
                        posicao = posicao + 1
                    print("O campeonato terá %d jogos, relacionados a seguir: " % len(jogos), jogos)
                    break                         
            else:
                print("Opção inválida, digite I, T ou S")
