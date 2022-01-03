from itertools import combinations

n = 33

def get_primes(n):
    is_prime = [False, False] + [True] * (n-2)

    for i in range(int(n//2)+1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False

    return [i for i, p in enumerate(is_prime) if p]


def solution(n):
    primes = get_primes(n)

    return [sum(c) for c in combinations(primes, 3)].count(n)

print(solution(n))