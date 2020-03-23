# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:07:51 2020

@author: Aiva
"""

import numpy as np
matrix=np.zeros((3,3))
matrix2=np.zeros((3,3))



for i in range(0,3):
    for j in range(0,3):
        print("Enter the element[",i+1,"][",j+1,"]:")
        matrix[i][j]=input()
        print(matrix[i][j],"\n")
        

        
for k in range(2):
            multiple=np.zeros(3)
            for i in range(k+1,3):
                if matrix[k][k]==0:
                    continue
                else:
                    multiple[i]=matrix[i][k]/matrix[k][k]
                
                
            for i in range(1,3):
                for j in range(3):
                    if multiple[i]==0:
                        continue
                    else:
                        matrix[i][j]=matrix[i][j]-(multiple[i]*matrix[k][j])
print(matrix)                                      
for i in range(3):
    if matrix[i][i]!=1 and matrix[i][i]!=0:
        matrix[i]/=matrix[i][i]              
                        

count=3
for i in range(3):
    if matrix[i].any():
        count-=1
        
print("The no. of variables required are ",count)

"""Calculating nullspace vector"""
equation=np.zeros(3,dtype={'names':('char','coeff'),'formats':('U1','int')})
variables=['x','y','z']
equation['char']=variables
for i in range(0,3):
    equation['coeff']=matrix[i]
    for j in range(3):
        if matrix[i][j]!=0:
            print(matrix[i][j],equation['char'][j])
    print("\n")
    
    """Calculation of inverse of the matrix"""
    
inverse=np.zeros((3,3))
inverse=np.linalg.inv(matrix)
    
print(inverse)    
    
"""Condition 1 (completely reduced row echlon form)"""

num=[2,1]

for i in range(3):
    count=0
    for j in range(3):
        while(np.any(num)):
            if matrix[i][j]==0:
                count+=1
            
    if count in num:
        num.remove(count)
        
if num==None:
    print("the values of x,y,z are all zero")
        
        

    
    