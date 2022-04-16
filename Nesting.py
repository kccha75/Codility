# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    n=len(S)
    total=0
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
                total+=1
            else:
                # check empty
                if total==0:
                    return 0
                total-=1 # close bracket

        if total==0:
            return 1
        else:
            return 0

