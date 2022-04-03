# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N=len(A)

    if N==1:
        return A[0]

    B=sorted(A)

    if B[N-1]!=B[N-2]:
        return B[N-1]
        
    for i in range(0,N-1,2):
        if B[i]!=B[i+1]:
            return B[i]
    