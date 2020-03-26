# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:37:32 2020

@author: Avinash Subhash
"""
"""The program takes a matrix of order nxn as input 
and outputs the basis of rowspace and column space"""


import numpy as np


matrix=np.zeros((3,3))
matrix2=np.zeros((3,3))



for i in range(0,3):
    for j in range(0,3):
        print("Enter the element[",i+1,"][",j+1,"]:")
        matrix[i][j]=input()
matrix2=matrix
print("Enterd matrix:\n")
print(matrix2,"\n")        

        
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
                        
                        
for i in range(3):
    if matrix[i][i]!=1 and matrix[i][i]!=0:
        matrix[i]/=matrix[i][i] 

print("Reduced row echlon matrix:\n")             
print(matrix)

""" Basis for Column space"""
print("Basis for Column space:\n") 
for i in range(3):
    if matrix[i][i]==1:
        print("Column vector:")
        print(matrix[:,[i]],"\n")
        
"""Basis for Row space"""
print("Basis for Row space:\n")

for i in range(3):
    if matrix[i][i]==1:
        print("Row vector:")
        print(matrix[i],"\n")