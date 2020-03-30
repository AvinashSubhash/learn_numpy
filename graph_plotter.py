# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:27:02 2020

@author: Aiva
"""

import numpy as np
list=[1,5,7,9,20,20]

for i in range(25):
    for j in range(25):
        if j==0:
            print("|",end="")
        elif i==24:
            print("--",end="")
        elif i in list and j in list:
            print("x",end=" ")
        else:
            print(".",end=" ")
    print("\n",end="")
    
        