def greedy(c,n):
    count=[None]*len(c)
    for i in range(len(c)):
        count[i]=0
        while n>=c[i]:
            n-=c[i]
            count[i]+=1
    return count
