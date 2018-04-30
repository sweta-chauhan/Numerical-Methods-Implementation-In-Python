#Integration By
#______________#
#-------------------Huen's Method------------------#
from math import *
import parser
import sys
import copy

def function(equ,x,y):
    return eval(equ)




def Integration(equ,init_x,init_funct,initial,final,step_size):
    lst = []
    iter_val = int((final - initial)/step_size)
    y_i_corrector = 0.000000
    predictor = 0.00000000
    lst=[]
    for i in range(iter_val):
        predictior = init_funct + function(equ,init_x,init_funct)*step_size
        y_i_corrector = init_funct + (function(equ,init_x,init_funct)+function(equ,init_x+step_size,predictior))*step_size/2
        lst.append(y_i_corrector)
        init_funct = y_i_corrector
        init_x = init_x + step_size
    return lst



if __name__=="__main__":
    lt=[]
    equation=str(input("Enter Equation:"))
    lt =Integration(equation,0.0,2.0,0,4,1)
    for i in range(len(lt)):
        print(lt[i])
