def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(n):
            if a[j]>a[i]:
                a[j],a[i]=a[i],a[j]
    return a
