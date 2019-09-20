#!/usr/bin/env python
# -*- coding: utf-8 -*-
l = 0
d = 0
def area_quadrado(l, d):
	l = float(raw_input("Lado: "))
	d = l ** 2
	return "Área do quadrado: %.2f" % d
print area_quadrado(l, d)
