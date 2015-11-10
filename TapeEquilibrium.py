import sys
def solution(A):
    # write your code in Python 2.7
    min = sys.maxint
    for i in range(len(A)):
        if(abs(sum(A[:i])-sum(A[i:]))<min):
            min = abs(sum(A[:i])- sum(A[i:]))
    return min

a = [3,1,2,4,3]
print solution(a)