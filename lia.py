#lia
def fact(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c

def probability(k, N):
    p = 1 / 4
    total_organisms = 2 ** k 

    prob = 0
    for x in range(N, total_organisms + 1):
        prob += fact(total_organisms, x) * (p ** x) * ((1 - p) ** (total_organisms - x))
    
    return round(prob, 3)

print(probability(7, 38))

