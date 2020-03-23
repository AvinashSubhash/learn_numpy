# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:43:34 2020

@author: Aiva
"""

import numpy as np
array=np.zeros(4)
for i in range(4):
    array[i]=input()
    
if array.any():
    print("Some elements are zero")