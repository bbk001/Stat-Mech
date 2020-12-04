from scipy.integrate import quad
from math import e
import matplotlib.pyplot as plt

def integrand(x,c,t):
    return x**.5/(e**((x-c)/t)+1)

def integrand2(x,c,t):
    return (3/2)*(x**(3/2)/(e**((x-c)/t)+1))

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

def cTable():
    c=[]
    tArray=[]
    t = 0.05
    while t<=4:
        t+=0.01
        c += [cFinder(t)]
        tArray+=[t]
    return tArray,c

def plotter():
    tArray,c=cTable()
    plt.scatter(tArray,c)
    plt.show()
            
def wPlotter(plot=True):
    tArray,c=cTable()
    wArray = []
    averageArray = []
    for i in range(len(tArray)):
        wArray += [quad(integrand2,0,20,args=(c[i],tArray[i]))[0]]
        averageArray += [3/2*tArray[i]]
    if plot:
        plt.scatter(tArray,averageArray)
        plt.scatter(tArray,wArray)
        plt.show()
    return wArray,tArray

def heat():
    wArray,tArray = wPlotter(False)
    delwArray = []
    deltArray = []
    mainArray = []
    for i in range(1,len(wArray)):
        delwArray += [wArray[i]-wArray[i-1]]
        deltArray += [tArray[i]-tArray[i-1]]
        mainArray += [delwArray[-1]/deltArray[-1]]
    plt.scatter(tArray[1:],mainArray)
    plt.show()
    






    