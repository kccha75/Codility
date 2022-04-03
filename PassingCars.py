# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    total=0
    n = len(A)
    # use suffix sum
    S = [0] * (n + 1)
    S[n]=A[n-1]
    for k in range(n-1, 0,-1):
        S[k] = S[k + 1] + A[k - 1]
    
    for i in range(n):
        if A[i]==0:
            total=total+S[i+1]
            if total>1000000000:
                return -1
    return total
