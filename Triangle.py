# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()
    n=len(A)
    for i in range(n-2):
        # Ensure positive, and condition
        if A[i]>=0 and A[i]+A[i+1]>A[i+2]:
            return 1
    return 0

