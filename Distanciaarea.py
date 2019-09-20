#!/usr/bin/env python
# -*- coding: utf-8 -*-
def distancia(x1, y1, x2, y2):
	import math
	dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
	return dist

def areaquadrado(x1,y1,x2,y2):
	import math
	lado = distancia(x1,y1,x2,y2)
	return lado**2
