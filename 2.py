def eratosthenes(n):
    primes = [True] * (n + 1)
    primes[:2] = False, False

    for i in range(n + 1):
        if primes[i]:
            primes[2 * i :: i] = [False] * len(primes[2 * i :: i])
    return [i for i in range(n + 1) if primes[i]]

def dict_del(a):
    primes = eratosthenes(int(a**0.5) + 1)
    factors = dict()

    for i in range(len(primes)):
        while a % primes[i] == 0:
            factors[primes[i]] = factors.get(primes[i], 0) + 1
            a //= primes[i]
        if a == 1:
            break
    if a > 1:
        factors[a] = 1

    return factors
biol=int(input())
inform=int(input())

dict_biol=(dict_del(biol))
dict_inform=dict_del(inform)
primes = set(dict_biol.keys()) | set(dict_inform.keys())
NOK = 1
for i in primes:
    NOK = NOK *  i ** max(dict_biol.get(i, 0), dict_inform.get(i, 0))
print("NOK="+ str(NOK))
