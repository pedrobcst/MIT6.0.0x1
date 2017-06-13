# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import math
def polysum(n,s):
    dom=0.25*n*pow(s,2)
    div=math.tan(math.pi/n)
    return round(dom/div +pow(n*s,2),4)

print(polysum(12,83))