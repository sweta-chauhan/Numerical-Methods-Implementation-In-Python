#Integration By
#______________#
#-------------------Euler's Method------------------#
from math import *
import parser
import sys
import copy

def function(equ,x,y):
    return eval(equ)


#-------Computational logic part-----------------#
def Integration(equ,init_x,init_funct,initial,final,step_size):
    lst=[]
    iter_val = int((final-initial)/step_size)
    y_i = 0.000000
    for i in range(iter_val):
        y_i = init_funct + function(equ,init_x,init_funct)*step_size
        lst.append(y_i)
        init_funct = y_i
        init_x = init_x + step_size
    return lst

#-----------------IO Part--------------------#
if __name__=="__main__":
    lt=[]
    equation=str(input("Enter Equation:"))
    lt =Integration(equation,0.0,1.0,0.0,4.0,0.5)
    for i in range(len(lt)):
        print(lt[i])
        
