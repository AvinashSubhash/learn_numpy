# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:47:23 2020

@author: Aiva
"""
import numpy as np
array=np.array(4)
array=[1,2,np.nan,-np.inf]
for i in range(4):
    if array[i]>0:
        print("yes")
    else:
        print("no")
print(array)