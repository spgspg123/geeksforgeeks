def solve(n):
    if n==1:
        dp[n] = 1
        return 1

    
    factors = []
    i = 1

    if n in dp:
        return dp[n]
    
    while(i*i<=n):
        if(n%i==0):
            factors.extend([i,n//i])
        if(i*i==n):
            factors.pop()
        i+=1

    s = 0
    #print(factors)
    for i in factors:
        if i!=n:
            s+=nways(i,dp)

    dp[n] = s
    #print(n,dp[n],dp)
    return s

T = int(input())
for _ in range(T):
    N=int(input())

    out_= solve(N)
    print(out_)