#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sqrt(((x1 − x2 )** 2) + ((y1 − y2 ) ** 2))
# p1 (x1 , y1 ) e p2 (x2 , y2 )
import math
p1 = []
p2 = []
x1 = 0
x2 = 0
y1 = 0
y2 = 0
d = 0
def distancia(p1, p2, x1, x2, y1, y2):
	x1 = float(raw_input("x1: "))
	x2 = float(raw_input("x2: "))
	y1 = float(raw_input("y1: "))
	y2 = float(raw_input("y2: "))
	p1.append(x1)
	p1.append(x2)
	p2.append(y1)
	p2.append(y2)
	d = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
	return "A distancia entre os Pontos (%d, %d) e (%d, %d) é de %.2f" % (x1, x2, y1, y2, d)
print distancia(p1, p2, x1, x2, y1, y2)
