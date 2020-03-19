# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 22:38:32 2020

@author: Aiva
"""

import numpy as np

array1=np.full((3,4),3)
array1=array1.reshape((4,3))



print(array1[:,np.newaxis])
""" printing new line for every column"""

array2=np.ones((3,4))
print(array2)


array2=np.ones((3,4))

"""Horizontally stacking up the array"""
array3=np.hstack([array1,array2])
print(array3)


"""splitting of arrays and matrix"""

array4=np.arange(16)
array4=array4.reshape((4,4))
print(array4)

print(np.vsplit(array4,[1,2,3]),"\n")

print(np.hsplit(array4,[1,2,3]),"\n")




