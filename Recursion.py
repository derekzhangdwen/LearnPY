def fastmod(b,n,m):
    if n==0:
        return 1
    elif n%2==0:
        return (fastmod(b,n/2,m)**2)%m
    else:
        return ((fastmod(b,(n-1)/2,m)**2%m)*(b%m))%m
