# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()
    n=len(A)
    # return max 3 product OR 2 negative (last 2) * max
    return max(A[n-1]*A[n-2]*A[n-3],A[0]*A[1]*A[n-1])
