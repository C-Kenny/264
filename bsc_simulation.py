#!/Users/dtg/Dropbox/UC_2014/S2/264/env/bin/python

'''
Simulates a BSC, modelled using a binomial distribution.
'''

import hamming
import distribution
from sys import argv


def efficiency(data_size, num_transmissions, message_len):
    return data_size / (num_transmissions * message_len)


def average_efficiency(efficiencies: list):
    return sum(efficiencies) / len(efficiencies)


def simulate(num_simulations, error_rate, user_data, message_len):
    efficiencies = []
    k = user_data + 100
    total_submissions = 0
    for _ in range(num_simulations):

        # Send one package
        num_errors = distribution.num_errors(message_len, error_rate)
        bound = hamming.hamming_bound(message_len, k)

        # While not successful
        num_transmissions = 1
        while num_errors > bound:
            num_errors = distribution.num_errors(message_len, error_rate)
            num_transmissions += 1

        efficiencies.append(efficiency(k, num_transmissions, message_len))

        total_submissions += num_transmissions

    print(total_submissions)
    return average_efficiency(efficiencies)


if __name__ == "__main__":
    '''
    Command line parameters:
        -u data size u
        -p bit error probability
        -r number of redundant bits n-k
    '''
    overhead = 100
    num_simulations = 10 ** 6

    user_data = int(argv[argv.index("-u") + 1])
    error_rate = float(argv[argv.index("-p") + 1])
    redundant_bits = int(argv[argv.index("-r") + 1])
    message_len = user_data + overhead + redundant_bits

    print(user_data, error_rate, redundant_bits)

    average_efficiency = simulate(num_simulations, error_rate, user_data, message_len)

    print(average_efficiency)
