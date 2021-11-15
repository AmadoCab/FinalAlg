from math import sqrt

def d(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def h(A,B):
    supval = 0
    for a in A:
        infval = 'None'
        for b in B:
            if infval == 'None':
                infval = d(a,b)
            else:
                infval = min(infval,d(a,b))
        supval = max(supval,infval)
    return supval

def H(A,B):
    return max(h(A,B),h(B,A))

X = [
    (1,1), (0,0)
]

Y = [
    (1,-1), (0,0)
]

print(H(X,Y))

# EOF #

