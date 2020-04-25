A = [3,5,15,20]
v = 4

def is_factor_in_array(A, v):
    for a in A:
        b = a*v
        if b in A:
            return (a,b)
    return False

print(is_factor_in_array(A,v))