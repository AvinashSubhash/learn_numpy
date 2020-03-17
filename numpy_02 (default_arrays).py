# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 06:40:36 2020

@author: Aiva
"""

import numpy as np
array1=np.zeros((3,4),dtype=int)

for i in array1:
    for j in i:
        print(j)
    print("\n")
    
    
    
array2=np.ones((3,4),dtype=int)

for i in array2:
    for j in i:
        print(j)
    print("\n")
    
    
array3=np.full((3,4),10)

for i in array3:
    for j in i:
        print(j)
     print("\n")