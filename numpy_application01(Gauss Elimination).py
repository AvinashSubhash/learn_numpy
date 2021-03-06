# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 20:14:35 2020

@author: Avinash Subhash
"""
"""The program intakes a matrix of order nxn and outputs the resultant 
matrix after gauss elimination along with the rank of the matrix"""


import numpy as np

sample_row=np.zeros(3)
#sample_row assigned to check for the complete 0 rows
matrix=np.zeros((3,3))
matrix2=np.zeros((3,3))



for i in range(0,3):
    for j in range(0,3):
        print("Enter the element[",i+1,"][",j+1,"]:")
        matrix[i][j]=input()
        print(matrix[i][j],"\n")
matrix2=matrix     
"""The matrix value assigned to matrix2 for furthur calculations"""
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
                    
                
                
print("Guass eliminated matrix:\n")                
print(matrix)

count=0
for i in range(3):
    if np.all(np.equal(matrix[i],sample_row)):
        count+=1
print("The rank of the matrix is ",3-count)
                
                