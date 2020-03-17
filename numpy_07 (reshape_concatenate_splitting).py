# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 22:38:32 2020

@author: Aiva
"""

import numpy as np

array1=np.full((3,4),3)
array1=array1.reshape((3,4))


print(array1[:,np.newaxis])
""" printing new line for every column"""

array2=np.ones((3,4))
print(array2)


np.concatenate([array1,array2],axis=0)





