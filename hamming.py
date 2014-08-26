#!/Users/dtg/Dropbox/UC_2014/S2/264/env/bin/python
'''
Calculate the hamming bound of a k bit code.
'''
from scipy.special import binom

binom_sums = {}


def hamming_bound(n, k):
    # Calculate the hamming bound of a k bit code, that after encoding is
    # n bits long.

    exp = 2 ** (n - k)  # n - k, number of redundant bits
    print("exp = ", exp)
    binom_sum = 0

    i = 0
    while binom_sum < exp:
        if (n, i) in binom_sums:
            binom_sum += binom_sums[(n, i)]
        else:
            binom_sums[(n, i)] = binom(n, i)
            binom_sum += binom(n, i)

        i += 1

    return i