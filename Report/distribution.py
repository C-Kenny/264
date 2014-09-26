'''
Generate a binomially distributed random number. For the use of modelling the
bit errors of a BSC.
'''

from numpy.random import binomial


def num_errors(message_len: int, error_rate: float):
    return binomial(message_len, error_rate)
