def fetch(A, i):
    res = 0
    for j in range(31, -1, -1):
        res = (res << 1) | fetch(A, i)
    return res

def find(A, n):
    b = {}
    for i in range(n):
         b[fetch(A, i)] = True
    for i in range(0, n+1):
        if not b[i]:
            return i
