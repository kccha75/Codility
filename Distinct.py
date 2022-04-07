# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()
    n=len(A)
    # check empty
    if n==0:
        count=0
    else:
        count=1
        for i in range(0,n-1):
            if A[i]!=A[i+1]:
                count+=1
    return count
