import pandas as pd
import numpy as np

from sklearn import neighbors
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn import preprocessing

alpha_map = {}

class PlateModel:
    def __init__(self, path):
        print('Initialising model...')
        build_map()
        self.master = pd.read_csv(path)
        self.mod_frame = pd.DataFrame

        self.master['Approved'] = 0
        for i in range(len(self.master)):
            if self.master.loc[i, 'status'] == 'Y':
                self.master.loc[i, 'Approved'] = 1
        print('Initialising complete')

    def build_model(self):
        self.mod_frame = PlateModel.format_data(self.master)
        self.X = self.mod_frame.Combination.values
        self.y = self.mod_frame.Approved.values

        self.X = self.X[:, None]
        self.model = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
        self.model.fit(self.X, self.y)

    def evaluate_model(self):
        print(self.model.score(self.X, self.y))

    def predict_approved(self, plate):
        p = PlateModel.get_permutations(plate)
        p = pd.DataFrame(p, columns=['Combination'])
        p = p.Combination.values

        X = p[:, None]
        out = self.model.predict(X)
        print(out)

    @staticmethod
    def get_permutations(plate):
        m = 2
        l = []

        # TODO: Fix broken chars
        for i in range(len(plate)):
            if plate[i] not in alpha_map:
                return l
            
        while m <= len(plate):
            for i in range(0, len(plate) - m + 1):
                p = 1
                for j in range(0, m):
                    p *= alpha_map[plate[i+j]]
                l.append(p)

            m += 1
        return l

    # TODO: Could be cleaner and doesn't really need to be static
    @staticmethod
    def format_data(df):
        t = df.copy()
        r = {'Approved': [], 'Combination': []}

        for i in range(len(t)):
            app = t.loc[i, 'Approved']
            plate = t.loc[i, 'plate']

            perms = PlateModel.get_permutations(plate)
            for perm in perms:
                r['Approved'].append(app)
                r['Combination'].append(perm)

        return pd.DataFrame.from_dict(r)


## - Prime Stuff
# Mapping to primes guarentees products of multiplications are unique

# Build the map
def build_map():
    alpha = list(map(chr, range(ord('A'), ord('Z') + 1)))
    alpha.extend(list(map(chr, range(ord('0'), ord('9') + 1))))
    alpha.append(' ')
    alpha.append('$')
    alpha.append('&')
    alpha.append('#')
    alpha.append('-')
    alpha.append('É')

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

