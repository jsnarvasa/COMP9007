'''
Suppose we are given an array A of n integers and an integer value v.
We want to determine whether there exists two integers a,b that is a member of A, 
where b is the larger value, and b / a = v

Examples:
A: [9,5,8,1], v = 10, result: False
A: [2,4,5,7], v = 2, result: 2 and 4
'''


A = [3,5,15,20]
v = 4

def is_factor_in_array(A, v):
    for a in A:
        b = a*v
        if b in A:
            return (a,b)
    return False

print(is_factor_in_array(A,v))