from scipy.integrate import quad
from math import e
import matplotlib.pyplot as plt

def integrand(x,c,t):
    return x**.5/(e**((x-c)/t)+1)

def cFinder(t):
    c = 0 #let's just start with c=0, why not
    currentResult = quad(integrand,0,20,args=(c,t))[0] #our result from part b. Upper bound of 20 is high enough to be accurate 
                                                       #but low enough so that the program doesn't crash
    if 2/3>currentResult:
        while 2/3>currentResult:
            c += 1
            currentResult = quad(integrand,0,20,args=(c,t))[0]
        c-=1
    else:
        while 2/3<currentResult:
            c -= 1
            currentResult = quad(integrand,0,20,args=(c,t))[0]
    currentResult = quad(integrand,0,20,args=(c,t))[0]
    if 2/3>currentResult:
        direction = 1
    else:
        direction = -1
    currentScale = .5
    while abs(currentResult-2/3)>1e-7:
        #print(currentResult)
        c += currentScale*direction
        currentResult = quad(integrand,0,20,args=(c,t))[0]
        if currentResult-2/3>0:
            direction = -1
        else:
            direction = 1
        currentScale *= .5
    return c

def plotter():
    c=[]
    tArray=[]
    t = 0.05
    while t<=4:
        t+=0.01
        c += [cFinder(t)]
        tArray+=[t]
    plt.scatter(tArray,c)
    plt.show()

            
            






    