#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Contatos():
    def __init__ (self,nome=None,fone=None,email=None):
        self.nome = nome
        self.fone = fone
        self.email = email


    # Método salvar, salva os contatos no arquivo.txt(BookContacts) 
    def salvar (self,nome,fone,email):
            
        
        b = 100
        a = 0
        t = 0

        
            


        # laço para entrada de dados
        while(a<b):
            if(t==99):
                break
            else:
                
                listaNome = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","z","y","w","y"
                             "1","2","3","4","5","6","7","8","9","0","Á","É","Í","á","é","í","ã","â","Â","Ã",
                             "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Z","Y","W","Y"]
                lista2=[]
                nome = str(input("\nNOME : "))
                for a in nome:
                    lista2.append(a)
                con=0
                for a in range(len(lista2)):
                    for b in range(len(listaNome)):
                        if(lista2[a]==listaNome[b]):
                            con=con+1
                if(con==len(lista2)):
                    pass
                else:
                    print("\nNome não aceito.")
                    break


                while(1):
                    listaNome = ["-","*","#"," ","1","2","3","4","5","6","7","8","9","0"]
                    lista2=[]
                    fone = str(input("\nFONE : "))
                    for a in fone:
                        lista2.append(a)
                    con=0
                    for a in range(len(lista2)):
                        for b in range(len(listaNome)):
                            if(lista2[a]==listaNome[b]):
                                con=con+1
                    if(con==len(lista2)):
                        break
                    else:
                        print("\nFone não aceito.")
                        

                    
                t = 1
                f = 100
                e = 0
                # laço que verifica e restringe a entrada de 0 ou mais de 1 @
                while(e<f):
                    email = input("\nE-MAIL: ")
                    x = email.count("@" and ".com")
                    if(x == 0):
                        print("\nO EMAIL DIGITADO ESTA INCORRETO ")
                        b = b + 1
                        continue
                    elif(x > 1):
                        print("\nO e-mail digitado contém %d '@'" %(x))
                        b = b + 1
                        continue
                    else:
                        # salvando dados no arquivo.txt
                        file = open("contatos.txt","a")
                        file.write(str(nome)+"\t\t\t"+str(fone)+"\t"+str(email)+"\t"+"\n")
                        file.close()
                        print("\nO contato %s foi salvo no BookContacts" %(nome))
                        e = 100
                        t = 99

        




    # Exibe os contatos 
    def exibir (self,nome):
        

        while(1):

            op=str(input("Digite \n(1)-> EXIBIR CONTATO \n(2)-> EXIBIR TODOS OS CONTATOS \n(0)-> PARA SAIR \n>>> : "))
            
            if(op == "1"):
                valor=False
                file = open("contatos.txt","r")
                lista = file.readlines()
                file.close()
                letra=str(input("\nCONTATO A EXIBIR:"))
                print("\n")
                for x in lista:
                    if (x.startswith (letra)):
                        valor=True
                        print(x)
                if(valor != True):
                    print ("\n CONTATO NÃO ENCONTRADO\n ")
                break
                        

            if(op == "2"):
                file=open("contatos.txt","r")
                lista=file.readlines()
                file.close()
                print ("Nome:\t Fone:\t E-mail:\n")
                for i in lista:
                    print (i)
                

            if (op == "0"):
                print ("\nVOCE SAIO DO MENU EXIBIR\n ")
                break

            else:
                print(" VOCE DIGITOU UMA OPÇÃO INVALIDA ")
          

    # Método excuir, exclui os contatos do BookContacts
    def excluir(self,nome):
        file = open("contatos.txt","r")
        lista =  file.readlines()
        lista1 = []
        file.close()
          
        # excluindo um contato

        while(1):
            esc= str(input("Digite: \n(1)-> PARA EXCLUIR UM CONTATO \n(2)-> PARA EXCLUIR TODOS OS CONTATOS \n(0)-> PARA SAIR \n>>>"))
            t = False
            
            if(esc == "1"):
                n = str(input(" \nCONTATO : "))
                for x in lista:
                    if (x.startswith (n)):
                        t = True
                        print(lista.index(x),x)


                        for i in lista:
                            if(nome in i):
                                j = input("\nNUMERAÇÃO DO CONTATO:")
                                lista.pop(int(j))
                                print("\nCONTATO EXCLUÍDO COM SUCESSO")
                                break
                            
                if(t != True):
                    print("\n NÃO FOI LOCALIZADO NO BookContacts")
                    

                


                file = open("contatos.txt","w")                         
                file.writelines(lista)
                file.close()

            if( esc == "2"):

                file = open("contatos.txt","w")
                file.writelines(lista1)
                file.close()
                print("Todos os contatos do BookContacts foram excluidos")

            if (esc == "0"):
                print ("\nVOCE SAIu DO MENU EXCLUIR\n ")
                break

            else:
                print("VOCÊ DIGITOU UMA OPÇÃO INVÁLIDA ")
                
                

    # Edita os contatos
    def editar(self,nome):
            arquivo=open("contatos.txt","r")
            lista=arquivo.readlines()             
            arquivo.close()
            
            for i in lista:                  
                linha=i.split("\t")
                letra=str(input("CONTATO :"))
                
                for x in lista:
                    if (x.startswith (letra)):
                        print(lista.index(x),x)
                        pass
           
                        
                if nome in linha:         
                    y=lista.index(i)
                    opcao=str(input("Opção que deseja alterar:\n(1)NOME   (2)FONE   (3)E-MAIL   (4)TUDO   (ENTER)SAIR\n"))
                    
                    if (opcao=="1"):
                        nome=str(input("NOVO NOME:"))
                        del linha[0]                    
                        linha.insert(0,nome)            
                        print("Nome alterado com sucesso.")
                        
                    elif (opcao=="2"):
                        fone = str(input("NOVO FONE:"))
                        del linha[3]
                        linha.insert(3,fone)
                        print("Fone alterado com sucesso")
                        
                    elif (opcao=="3"):
                        email=str(input("E-MAIL:"))
                        del linha[4]
                        linha.insert(4,email)
                        print("Email foi alterado com sucesso")

                    elif (opcao=="4"):
                        nome=str(input("NOVO NOME:"))
                        del linha[0]                    
                        linha.insert(0,nome)
                        fone = str(input("NOVO FONE:"))
                        del linha[3]
                        linha.insert(3,fone)
                        email=str(input("E-MAIL:"))
                        del linha[4]
                        linha.insert(4,email)
                        print("Dados alterado com sucesso!")
                        

                    else:
                        print("voce saiu do menu alterar")
                        break 
                
                        
                        
                    linha="\t".join(linha)           
                    del lista[y]                     
                    lista.insert(y,linha)
                    
                    arquivo=open("contatos.txt","w")      
                    arquivo.writelines(lista)
                    arquivo.close()
                    break                          
                
            else:                                  
                print(" %s NÃO ESTÁ CADASTRADO DO BookContacts" %(nome))

            file = open("contatos.txt","r")
            lista = file.readlines()  
            for i in range(len(lista)):
                lista2 = lista[i].rsplit("\t")
                if (lista2[0]== nome):
                    print("\n"+"nome: "+lista2[0]+"\n"+"fone: "+lista2[3]+"\n"+"email: "+lista2[4]+"\n")                
                   










                     
c = Contatos ()
while(1):
    print("\n***************BookContacts*****************\n",
          "\nSALVAR CONTATO  ----------(1) ",
          "\nEXIBIR CONTATO  ----------(2) ",
          "\nEDITAR CONTATO  ----------(3) ",
          "\nEXCLUIR CONTATO ----------(4) ",
          "\nSAIR DO BookContacts -----(0)")

    variavel = str(input("\nDigite o que deseja fazer: "))

    if(variavel == "1"):
        c.salvar('','','')

    elif(variavel == "2"):
        # abre o arquivo para leitura
        file = open("contatos.txt","r")
        palavras = file.read().split()
        p = (len(palavras))
        #verifica se há contatos(strings) no arquivo
        if(p == 0 ):
            print("AINDA NÃO EXISTE CONTATO NO BookContacts")
        else:
            c.exibir('')
        

    elif(variavel == "3"):
        c.editar('')

    elif(variavel == "4"):
        
        c.excluir('')

    elif(variavel == "0"):
        break

    else:
        print("Error") 
