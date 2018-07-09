def gcd(a,b):
    while a!=0:
        a,b=b%a,a
    return b

def invmod(a,b):
    ta,tb=a,b
    trace=[]
    switch=False
    l,r=1,1
    flag=True
    while a!=0:
        print(a,b)#
        trace.append(b//a)
        a,b=b%a,a
    if b!=1:
        raise ValueError('invalid input: gcd(%d,%d)!=1' %(a,b))
    print(trace)#
    if trace[0]==0:
        switch=True
        del trace[0]
    if len(trace)==2:
        if switch:
            return(1,-trace[0])
        else:
            return (-trace[0],1)
    else:
        del trace[len(trace)-1]
        del trace[len(trace)-1]
        for i in range(len(trace)-1,-1,-1):
            if flag:
                l=l+r*trace[i]
                flag=not flag
            else:
                r=r+l*trace[i]
                flag=not flag
        if len(trace)%2==0:
            l,r=-r,-l
        if switch:
            print(ta*(-r)+tb*l)#
            return(-r,l)

        else:
            print(ta*l+tb*(-r))#
            return(l,-r)
