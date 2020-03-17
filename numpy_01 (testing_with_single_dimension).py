# -*- coding: utf-8 -*-
"""
Created on Sun Feb  15 14:30:35 2020

@author: Aiva
"""

import numpy as np
vowels="aeiou"
a=np.array(["avinash","akash"])
for i in a:
    for j in i:
        if j in vowels:
            print(j,": in element ",i,"\n")
