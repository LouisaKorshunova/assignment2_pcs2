#perm
from itertools import permutations
import math
file=open('/Users/makbuk/Downloads/rosalind_perm.txt')
line=file.readlines()
n=int(line[0])
lst=[]
i=0
a=0
print(math.factorial(n))
while i<n:
    i+=1
    lst.append(i)
perm=permutations(lst)
for i in perm:
    a=a+1
    print(*i)
