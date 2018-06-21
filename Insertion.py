def insertion(a):
    n=len(a)
    for j in range(1,n):
        i=0
        while(a[i]<a[j]):
            i+=1
        m=a[j]
        for k in range(j,i,-1):
            a[k]=a[k-1]
        a[i]=m
    return a
