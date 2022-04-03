# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    N=len(A)

    if N==0:
        return A
    if K>N: # modular
        K=K%N

    B=[0]*N
    if K%N==0: # check if rotate same as length (therefore return same vector)
        return A

    for i in range(K,N): # rotate from k
        B[i]=A[i-K]

    for i in range(0,K): # rotate to k
        B[i]=A[(i+N-K)%N]


    return B
