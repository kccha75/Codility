# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    
    counter=[0]*N
    maxcounter=0
    n = len(A)
    maximum=0

    for i in range(n):

        if A[i]<=N:

            counter[A[i]-1]=max(counter[A[i]-1]+1,maxcounter+1)

            maximum=max(maximum,counter[A[i]-1])

        else:
            
            maxcounter=maximum

    for i in range(N):

        counter[i]=max(counter[i],maxcounter)
        
    return counter