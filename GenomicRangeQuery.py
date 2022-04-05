# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):

    n=len(S)
    # prefix sum for each DNA letter (except T)
    prefixA=[0]*(n+1)
    prefixC=[0]*(n+1)
    prefixG=[0]*(n+1)

    j=0

    for i in S:
        j+=1
        if i=="A":
            prefixA[j]=prefixA[j-1]+1
            prefixC[j]=prefixC[j-1]
            prefixG[j]=prefixG[j-1]
        elif i=="C":
            prefixA[j]=prefixA[j-1]
            prefixC[j]=prefixC[j-1]+1
            prefixG[j]=prefixG[j-1]  
        elif i=="G":
            prefixA[j]=prefixA[j-1]
            prefixC[j]=prefixC[j-1]
            prefixG[j]=prefixG[j-1]+1
        else:
            prefixA[j]=prefixA[j-1]
            prefixC[j]=prefixC[j-1]
            prefixG[j]=prefixG[j-1]          
        
    m=len(P)
    result=[0]*m

    # for range given, check if prefix sum changed in given range
    for k in range(m):

        if prefixA[Q[k]+1]-prefixA[P[k]]!=0:
            result[k]=1
        elif prefixC[Q[k]+1]-prefixC[P[k]]!=0:
            result[k]=2
        elif prefixG[Q[k]+1]-prefixG[P[k]]!=0:
            result[k]=3
        else:
            result[k]=4

    return result