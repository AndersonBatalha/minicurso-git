#!/usr/bin/env python
# -*- coding: utf-8 -*-
tabela = {}  # criação de uma estrutura de dicionário vazia
notas = []   # criação de uma estrutura do tipo lista para o armazenamento das notas de cada aluno.
while True:
    print("Existem %d alunos cadastrados." %  len(tabela))
    opcao = raw_input("Digite I para incluir novo aluno, notas e frequencias, A para atualizar algum registro, E para excluir, R para relatorio e S para sair: ")
    if opcao=="S":
        break
    else:
        if opcao=="I":   # Inclusão de um novo aluno, suas notas e frequencias.
            matricula = input("Digite matricula do aluno: ") 
            n1 = float(input("Digite nota 1 do aluno: ")) 
            notas.append(n1) # Adiciona um novo item (primeira nota) na lista.
            n2 = float(input("Digite nota 2 do aluno: "))
            notas.append(n2) # Adiciona um novo item (segunda nota) na lista.
            n3 = float(input("Digite nota 3 do aluno: "))
            notas.append(n3) # Adiciona um novo item (terceira nota) na lista.
            n4 = float(input("Digite nota 4 do aluno: "))
            notas.append(n4) # Adiciona um novo item (quarta nota) na lista.
            f1 = int(input("Digite frequencia 1 do aluno: "))
            notas.append(f1) # Adiciona um novo item (frequencia 1) na lista.
            f2 = int(input("Digite frequencia 2 do aluno: "))
            notas.append(f2) # Adiciona um novo item (frequencia 2) na lista.
            f3 = int(input("Digite frequencia 3 do aluno: "))
            notas.append(f3) # Adiciona um novo item (frequencia 3) na lista.
            f4 = int(input("Digite frequencia 4 do aluno: "))
            notas.append(f4) # Adiciona um novo item (frequencia 4) na lista.
            tabela[matricula] = notas  # Atualização de elemento na tabela, o elemento é indicado pela chave matricula
                                       # Se ainda não existir um elemento com o valor da chave, um novo será criado
                                       # A lista notas será o valor relacionado com a chave.
            notas = [] # a lista notas é "esvaziada".
        else:
            if opcao=="R":   # aqui a opção de relatório
                opcao = input("Digite C para relatorio completo e I para relatorio individual: ")
                if opcao=="C": 
                    for matricula, nota in tabela.items():  # no relatorio completo, todos os itens (chave e valor) do dicionário serão percorridos
                        print("Matricula: ", matricula)     # A chave matricula será apresentada
                        print("Nota 1: ", nota[0])          # Considerando que os valores do dicionario são listas, cada item da lista será
                        print("Nota 2: ", nota[1])          # referenciado pelo seu índice
                        print("Nota 3: ", nota[2])
                        print("Nota 4: ", nota[3])
                        print("Freq 1: ", nota[4])
                        print("Freq 2: ", nota[5])
                        print("Freq 3: ", nota[6])
                        print("Freq 4: ", nota[7])
                        media = (nota[0] + nota[1] + nota[2] + nota[3])/4  # neste momento acontece o cálculo da média.
                        faltas = nota[4] + nota[5] + nota[6] + nota[7]     # aqui a soma das frequencias individuais
                        print("Media final: %4.2f, e frequencia total: %4.2f " % (media,faltas))
                else:
                    opcao = input("Digite matricula do aluno: ") # na opção pelo relatório individual, é solicitada a matricula do aluno (chave do dicionário)
                    if opcao in tabela:                          # na identificação da chave, serão apresentados os valores que estão com ela relacionados.
                       print("Matricula: ", opcao)
                       print("Nota 1: ", tabela[opcao][0])
                       print("Nota 2: ", tabela[opcao][1])
                       print("Nota 3: ", tabela[opcao][2])
                       print("Nota 4: ", tabela[opcao][3])
                       print("Freq 1: ", tabela[opcao][4])
                       print("Freq 2: ", tabela[opcao][5])
                       print("Freq 3: ", tabela[opcao][6])
                       print("Freq 4: ", tabela[opcao][7])
                       media = (tabela[opcao][0] + tabela[opcao][1] + tabela[opcao][2] + tabela[opcao][3])/4
                       faltas = tabela[opcao][4] + tabela[opcao][5] + tabela[opcao][6] + tabela[opcao][7]
                       print("Media final: %4.2f, e frequencia total: %4.2f " % (media,faltas))
            else:
                if opcao=="E":  # na opção pela exclusão do registo, a matricula (chave do dicionário) é solicitada.
                    opcao = input("Digite matricula do aluno a ser excluída: ")
                    if opcao in tabela:
                        del tabela[opcao] # se a chave existir no dicionário, o item será excluído.
                        print("Registro %s excluído." % opcao)
                    else:
                        print("Matricula não existe")
                else:
                     if opcao=="A":
                         opcao = input("Digite matricula do aluno a ser atualizado: ")
                         if opcao in tabela:        # se a opção for atualizar um registro, mais uma vez a pesquisa é feita com base na sua chave.
                             n1 = tabela[opcao][0]  # as variáveis recebem os valores da lista relacionada com a chave
                             n2 = tabela[opcao][1]
                             n3 = tabela[opcao][2]
                             n4 = tabela[opcao][3]
                             f1 = tabela[opcao][4]
                             f2 = tabela[opcao][5]
                             f3 = tabela[opcao][6]
                             f4 = tabela[opcao][7]

                             notas = [] # a lista notas é "esvaziada"

                             escolha = raw_input("N1 = %4.2f, Deseja alterar esta nota? (S/N): " % n1)

                             # para cada uma das notas e frequencias será oferecida a opção de alteração
                             # se a alteração for confirmada as variáveis anteriores serão atualizadas
                             # e um novo elemento será inserido na lista.
                             # se a alteração não for confirmada, a lista será alterada com o valor antigo

                             if escolha=="S":
                                 n1 = float(input("Digite nota 1 do aluno: "))

                             notas.append(n1)
                             escolha = input("N2 = %4.2f, Deseja alterar esta nota? (S/N): " % n2)

                             if escolha=="S":
                                 n2 = float(input("Digite nota 2 do aluno: "))

                             notas.append(n2)
                             escolha = input("N3 = %4.2f, Deseja alterar esta nota? (S/N): " % n3)

                             if escolha=="S":
                                 n3 = float(input("Digite nota 3 do aluno: "))

                             notas.append(n3)
                             escolha = input("N4 = %4.2f, Deseja alterar esta nota? (S/N): " % n4)

                             if escolha=="S":
                                 n4 = float(input("Digite nota 4 do aluno: "))

                             notas.append(n4)
                             escolha = input("F1 = %4.2f, Deseja alterar esta frequencia? (S/N): " % f1)

                             if escolha=="S":
                                 f1 = int(input("Digite frequencia 1 do aluno: "))

                             notas.append(f1)
                             escolha = input("F2 = %4.2f, Deseja alterar esta frequencia? (S/N): " % f2)

                             if escolha=="S":
                                 f2 = int(input("Digite frequencia 2 do aluno: "))

                             notas.append(f2)
                             escolha = input("F3 = %4.2f, Deseja alterar esta frequencia? (S/N): " % f3)

                             if escolha=="S":
                                 f3 = int(input("Digite frequencia 3 do aluno: "))

                             notas.append(f3)
                             escolha = input("F4 = %4.2f, Deseja alterar esta frequencia? (S/N): " % f4)

                             if escolha=="S":
                                 f4 = int(input("Digite frequencia 4 do aluno: "))    

                             notas.append(f4)    

                             # a instrução abaixo atualiza o elemento do dicionário, identificado através da sua chave
                             
                             tabela[opcao] = notas

                             
                             print("Registro %s atualizado." % opcao)
                         else:
                             print("Matricula não existe")
                         
