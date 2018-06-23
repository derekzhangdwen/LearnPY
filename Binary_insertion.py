def binaryinsertion(a):
    n=len(a)
    l,r=0,0
    for i in range(1,n):
        l,r=0,i-1
        while l<r:
            if a[i]<a[int((l+r+1)/2)]:
                r=int((l+r+1)/2)-1
            else:
                l=int((l+r+1)/2)
        if a[i]>=a[l]:
            l+=1
        m=a[i]
        for j in range(i,l,-1):
            a[j]=a[j-1]
        a[l]=m
    return a
