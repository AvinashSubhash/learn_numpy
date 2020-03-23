# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:37:07 2020

@author: Aiva
"""
import numpy as np
print("Enter the elements\n")
array=np.zeros(4)
for i in range(4):
    array[i]=input()
    
if array.all():
    print("None of the elements are zero")
    