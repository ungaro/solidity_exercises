import numpy as np
import math
def optimalEuropean(S, X, r, sigma,
                            T, N, optionType):
    dt = T/N
    u = math.exp(sigma*math.sqrt(dt))
    d = 1/u
    disc = math.exp(-r*T)
    p = (math.exp(r*dt)-d)/(u-d)
    q = 1-p
    a = math.log(X/(S*(d**N)))/math.log(u/d)
    a = math.ceil(a)
    S = S * (u**a) * (d**(N-a))
    b = (math.factorial(N)/(math.factorial(N-a)*math.factorial(a))) \
    * (p**a) * (q**(N-a))
    C = disc * b * (S-X)
    for j in range(a+1,N+1):
        b = ((p*(N-j+1)) / (q*j)) * b
        S = S * (u/d)
        C = C + disc * b * (S-X)
    return C
        
        
C = optimalEuropean(100,100,0.06,0.10,1,3,'C')
print(C)