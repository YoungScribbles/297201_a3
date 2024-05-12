import pandas as pd

def init():
    print('Initialising model...')
    build_map()
    print('Initialising complete')

## - Prime Stuff
# Mapping to primes guarentees products of multiplications are unique

alpha_map = {}

# Build the map
def build_map():
    alpha = list(map(chr, range(ord('A'), ord('Z') + 1)))
    alpha.extend(list(map(chr, range(ord('0'), ord('9') + 1))))
    alpha.append(' ')
    alpha.append('$')
    alpha.append('&')
    alpha.append('#')
    alpha.append('-')

    # We don't expect to see these but include them for sanity
    alpha.extend(list(map(chr, range(ord('a'), ord('z') + 1))))
    n = len(alpha)
    primes = get_n_primes(n)

    for i in range(len(alpha)):
        alpha_map[alpha[i]] = primes[i]

# Return True if num is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num*0.5) + 1):
        if num % i == 0:
            return False
    return True

# Returns an n-length list of sequential primes starting from 2
def get_n_primes(n):
    primes = []
    i = 2

    while len(primes) != n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

## - Model things
def generate_permutations(plate):
    m = 2
    l = []

    while m <= len(plate):
        for i in range(0, len(plate) - m + 1):
            p = 1
            for j in range(0, m):
                p *= alpha_map[plate[i+j]]
            l.append(p)

        m += 1
    return l
