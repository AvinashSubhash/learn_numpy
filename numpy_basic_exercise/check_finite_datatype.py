# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:45:53 2020

@author: Aiva
"""

import numpy as np
array=np.array(4)
array=[1,2,np.nan,0]


    
if np.all(np.isfinite(array)):
    print("ALL OK")
else:
    print("Error")