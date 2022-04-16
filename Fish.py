# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    n=len(A)
    stack=[]
    nstack=0 # length of stack
    top=0 # number of 0's before any 1

    for i in range(n):

        if B[i]==1: # add 1's to stack
            nstack+=1
            stack.append(A[i])

        if B[i]==0 and nstack!=0:

            while nstack>0 and A[i]>stack[nstack-1]: # loop stack and eat!
                stack.pop()
                nstack-=1

        if B[i]==0 and nstack==0:
            top+=1

    return nstack+top
