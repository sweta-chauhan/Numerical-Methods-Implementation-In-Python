import sys
import copy
# Program flow gaussSedel 1->rootValue=mapSum(matMull) 2->chkError
#with Initial guess 0 as soln.

#---------------------------------------------------------------------------------------------------------------------------------------------------

#try it yourslf
#matMull :: [float] -> [float]
def matMul(mat1,mat2):
    if(len(mat1)==len(mat2)):
        return [mat1[i]*mat2[i] for i in range(len(mat1))]
    

#-----------------------------------------------------------------------------------------------------#

#rootValue :: [float]  -> Int -> [float] -> [float]
def rootValue(eqn,nth,s_ls):
    mat1=eqn[0:(len(eqn)-1)]
    mat1[nth]=0
    return matMul(mat1,s_ls)
#------------------------------------------------------------------------------------------------------#

#mapSum ::[float] -> float
def mapSum(mat):
    sum=0
    for i in range(len(mat)):
        sum+=mat[i]
    return sum
#-------------------------------------------------------------------------------------------------------#

#errorlist :: [float]->[float]->[float]
def errorlist(current_soln,previous_soln):
    return [abs(((current_soln[i]-previous_soln[i])/current_soln[i])*100) for i in range(len(current_soln))]

#-------------------------------------------------------------------------------------------------------#

#chkError :: [float]-> Bool
def chkError(list_Of_soln,error):
    errlist=[list_Of_soln[i] for i in range(len(list_Of_soln)) if list_Of_soln[i]<error]
    if(len(errlist)==len(list_Of_soln)):
        return False
    else:
        return True
#gaussSedel :: [[float]]->Int ->[float]    
def gaussSedel(listofEqn,significant):
    error=0.5*(10**(2-significant))
    noOfeqn=len(listofEqn)
    fact=True
    iter1=0
    current_s = len(listofEqn)*[0.0]
    while(fact):
        previous_s=copy.deepcopy(current_s)
        for i in range(len(listofEqn)):
            current_s[i]=(listofEqn[i][noOfeqn]-mapSum(rootValue(listofEqn[i],i,current_s)))/listofEqn[i][i]
        #print("solution list : ",current_s)
        err_ls=errorlist(current_s,previous_s)
        #print("Error in different step  ",(iter1,err_ls))
        fact=chkError(err_ls,error)
        iter1+=1
    return current_s,err_ls


#-------------------------End of Computation Part-------------------#


#-------------------------IO Interface-------------------------------#
if __name__=="__main__":
    f=open(sys.argv[1],"r")
    mat=[]
    for line in f:
        mat+=[line]
    mat=[list(map(float,str1.strip().split(" "))) for str1 in mat ]
    print("Enter the Number of significant digit up to which you the correctness: ")
    n=int(input())
    solution,error=gaussSedel(mat,n)
    print("Solution List : ",solution)
    print("Error : ",error )
        

