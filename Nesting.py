# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# define matching function
def matching(A,B):
    if A=='(' and B==')':
        return 1
    else:
        return 0

def solution(S):
    n=len(S)
    stack=[]

    # check empty
    if n==0:
        return 1
    # check even
    elif n%2!=0:
        return 0
    else:
        # loop
        for i in range(n):
            if S[i]=='(':
                stack.append(S[i])
            else:
                # check empty before pop
                if len(stack)==0:
                    return 0
                last=stack.pop()
                # check matching
                if matching(last,S[i])==0:
                    return 0
        if len(stack)==0:
            return 1
        else:
            return 0
