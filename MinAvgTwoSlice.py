# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    n=len(A)
    P=[0]*(n+1)
    
    # Prefix sum    
    for k in range(1,n+1):
        P[k]=P[k-1]+A[k-1]

    # Assume first slice of 2 is minimum ...
    minimum=(P[2]-P[0])/(2)
    minstart=0
    
    for i in range(0,n-1):
        # slices of length 2
        average =(P[i+2]-P[i])/2.0
        
        if average < minimum:
            minimum=average
            minstart=i

        if n!=2 and i<n-2:
            # slices of length 3
            average =(P[i+3]-P[i])/3.0

            if average < minimum:
                minimum=average
                minstart=i

    return minstart

