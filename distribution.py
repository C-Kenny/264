#!/Users/dtg/Dropbox/UC_2014/S2/264/env/bin/python
'''
Generate a binomially distributed random number. For the use of modelling the
bit errors of a BSC.
'''

from numpy.random import binomial


def num_errors(message_len, error_rate):
    return binomial(message_len, error_rate)
