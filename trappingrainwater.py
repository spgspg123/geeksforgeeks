def rain_water(arr):
    n=len(arr)
    left= [0]*n
    left[0]=arr[0]
    right = [0]*n
    right[n-1]= arr[n-1]

    for i in range(1,n-1):
        left[i]=max(left[i-1],arr[i])

    for i in range(n-2,0,-1):
        right[i]=max(right[i+1],arr[i])

    area =0
    for i in range(1,n-1):
        area = area + (min(left[i],right[i]))-arr[i]

    return area

print("The amount of rain water is:",rain_water([1,0,2,0,1,0,3,1,0,2]))
