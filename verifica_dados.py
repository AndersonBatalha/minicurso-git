#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sexo = ""
def verifica(sexo):
	sexo = raw_input("Sexo (M / F): ")
	if sexo == "M" or sexo == "m":
		return "Masculino"
	elif sexo == "F" or sexo == "f":
		return "Feminino"
	else: return "Inválido"
print verifica(sexo)
