import pandas as pd
import numpy as np

from sklearn import neighbors
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn import preprocessing

alpha_map = {}

class PlateModel:
    max_plate_len = 13

    def __init__(self, path):
        print('Initialising model...')
        build_map()
        self.master = pd.read_csv(path)
        self.mod_frame = pd.DataFrame

        self.master['Approved'] = 0
        for i in range(len(self.master)):
            if self.master.loc[i, 'status'] == 'Y':
                self.master.loc[i, 'Approved'] = 1

        self.initialise_maps()
        self.build_model()
        print('Initialising complete')

    def initialise_maps(self):
        self.app_map = {}
        self.seen_map = {}
        self.perc_map = {}

        for i in range(len(self.master)):
            plate = self.master.loc[i, 'plate']
            approved = self.master.loc[i, 'Approved']

            perms = PlateModel.get_permutations(plate)
            for perm in perms:
                if perm not in self.app_map:
                    self.app_map[perm] = 0
                    self.seen_map[perm] = 0

                if approved == 1:
                    self.app_map[perm] += 1
                self.seen_map[perm] += 1

        for key in self.app_map.keys():
            self.perc_map[key] = self.app_map[key]/self.seen_map[key]

        self.seg_df = pd.DataFrame.from_dict(self.perc_map, orient='index', columns=['Prob'])
        self.seg_df = self.seg_df.sort_values(by='Prob')

    def build_model(self):
        # Construct a frame
        self.mod_f = self.master.copy()
        self.mod_f = self.mod_f[['plate', 'Approved']]

        # There are maximum 12 characters
        for i in range(13):
            self.mod_f[i] = 0.0

        for i in range(len(self.mod_f)):
            lp = self.mod_f.loc[i, 'plate']
            s, p = self.get_known_segments(lp)

            col = 0
            for perc in p:
                self.mod_f.loc[i, col] = perc
                col += 1

        cols = []
        for i in range(PlateModel.max_plate_len):
            cols.append(i)

        X = self.mod_f[cols]
        y = self.mod_f.Approved

        self.knn = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
        self.knn.fit(X,y)

    def get_known_segments(self, str_in, length=3):
        segs = []
        percs = []

        for i in range(len(str_in) - (length-1)):
            t = str_in[i:i+3]
            segs.append(t)

            if t in self.perc_map:
                percs.append(self.perc_map[t])
            else:
                # Assume coin flip
                percs.append(0.5)

        # Plate is smaller than the window
        if len(percs) == 0:
            segs.append(str_in)

            if str_in in self.perc_map:
                percs.append(self.perc_map[str_in])
            else:
                # Assume coin flip
                percs.append(0.5)

        return segs, percs

    def evaluate_model(self):
        print(self.model.score(self.X, self.y))

    def predict_approved(self, plate):
        s, p = self.get_known_segments(plate)
        cols = []
        for i in range(PlateModel.max_plate_len):
            cols.append(i)

        while len(p) < 13:
            p.append(0.0)

        fr = pd.DataFrame(p)
        fr = fr.T
        x = fr[cols]

        return self.knn.predict(x)

    @staticmethod
    def get_permutations(plate):
        m = 2
        l = []

        while m <= len(plate):
            for i in range(0, len(plate) - m + 1):
                s = ''
                for j in range(0, m):
                    s += plate[i+j]
                l.append(s)

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

