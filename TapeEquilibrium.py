# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # add total
    total=0
    for i in A:
        total=total+i

    righttotal=total
    lefttotal=0
    smallest=1000
    n=len(A)
    count=0

    for i in A:
  
        count=count+1
        lefttotal=lefttotal+i
        righttotal=righttotal-i

        diff=abs(lefttotal-righttotal)

        if n==2:

            return diff

        if smallest>diff and count!=n: #skip last

            smallest=diff
            
    return smallest