start = 13

def numberofsteps(x):
    step = 0
    while x != 1:
        step += 1
        if x%2==0:
            x = x/2
        else:
            x = 3*x+1
    return step
maxi = [0,13]
while start<1000000:
    if numberofsteps(start) > maxi[0]:
       maxi[0] = numberofsteps(start)
       maxi[1] = start
    start += 2
print(maxi)  