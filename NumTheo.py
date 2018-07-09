def gcd(a,b):
    while a!=0:
        a,b=b%a,a
    return b

def invmod(a,b):
    #ta,tb=a,b
    trace=[]
    switch=False
    l,r=1,0
    while a!=0:
        #print(a,b)#
        trace.append(b//a)
        a,b=b%a,a
    if b!=1:
        raise ValueError('invalid input: gcd(%d,%d)!=1' %(a,b))
    #print(trace)#
    if trace[0]==0:
        switch=True
        del trace[0]
    #del trace[len(trace)-1]
    for i in range(len(trace)-2,-1,-1):
        l,r=r-l*trace[i],l
    if switch:
        l,r=r,l
    #print(ta*l+tb*r)#
    return(l,r)
