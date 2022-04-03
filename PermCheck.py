# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    n = len(A)
    count = [0] * (n + 1)
    for k in range(n):

        if A[k]>n or count[A[k]]!=0:
            return 0
        count[A[k]] += 1
    return 1
