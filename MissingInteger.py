# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    n=len(A)
    count=[0]*(n+1)
    for k in range(n):

        if A[k]<n+1 and A[k]>0:
            count[A[k]]+=1
    
    for i in range(1,n+1):
        if count[i]==0:
            return i
    return n+1