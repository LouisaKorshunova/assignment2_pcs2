#fibd
import numpy as np

def mortal_fibonacci(n, m):
    rabbits = np.zeros(m, dtype=int)
    rabbits[0] = 1 

    for month in range(1, n):
        newborns = np.sum(rabbits[1:])
        
        rabbits[1:] = rabbits[:-1]
        
        rabbits[0] = newborns
    
    return np.sum(rabbits)

print(mortal_fibonacci(87, 17)) 
