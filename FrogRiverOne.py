# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    j=0
    n=len(A)
    count=[0]*(X+1)
    for k in range(n):
        count[A[k]]+=1

        if A[k]<=X and count[A[k]]==1:
            j+=1
            if j==X:
                return k
    return -1

