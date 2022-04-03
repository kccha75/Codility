# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N=len(A)
        
    A=sorted(A)
    for i in range(N):
        if A[i]!=i+1:
            return i+1
    return N+1