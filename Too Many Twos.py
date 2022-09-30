from math import comb
from re import X

def v2(n): 
    abs_n = abs(n)
    r = 0
    list_r = []
    while(2**r <= abs_n):
        if((n % (2**r)) == 0):
            list_r.append(r)
        r += 1
    return max(list_r)
       
def S(n):
    list_s = []
    for i in range(1,n+1):
        list_s.append(((-2)**i) * comb(2*i,i))
    return sum(list_s) 

def u(n):
    return v2(3*S(n) + 4)

def U(N):
    list_x = []
    for i in range(1,N+1):
        list_x.append(u(i**3))
    return sum(list_x)

print(U(16))

