

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):

    total=0
    moda=A%K
    modb=B%K

    # change A and B to something divisible by K
    if moda!=0:
        A=A+K-moda

    if modb!=0:
        B=B+K-modb
    else:
        total=total+1

    total=total+int((B-A)/K)

    return total

