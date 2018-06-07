import numpy as np
#calculate natural numbers
def nextnumber (n):
    x = sum(np.arange(0,n,1))
    return x

def numberoffactors(x):
    k = 0
    #print("x: " + str(x))
    if int(np.sqrt(x)**2) == x:
        k -= 1
    for i in range(1,int(np.sqrt(x))):
        if x%i == 0: 
            k += 2
            #print(i)
    return k+1

list = [1]
nfound = 1
n = 1
while nfound < 500:
    trial = nextnumber(n)
    n += 1
    nfound = numberoffactors(trial)


print("Number found: " + str(trial) + " has " + str(nfound) + " different factors.")


