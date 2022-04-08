def maxArea(A,le):
    #use two pointer approach for optimal result
    res =0
    l,r=0,le-1
    while l<r:
        area = (r-l)*min(A[l],A[r])
        res= max(area,res)
        if A[l]<A[r]:
            l+=1
        else:
            r-=1
            
    return res

