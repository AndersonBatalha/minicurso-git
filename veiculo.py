#!/usr/bin/env python
# -*- coding: utf-8 -*-
class veiculo:
	def __init__ (self):
		self.ligado = False
		self.rodas = 4
		self.flex = False
		self.marchaatual = 0
	def aumenta_marcha(self):
		self.marchaatual += 1
	def reduz_marcha(self):
		self.marchaatual -= 1
