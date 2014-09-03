#!/Users/dtg/Dropbox/UC_2014/S2/264/env/bin/python

'''
Simulates a BSC, modelled using a binomial distribution.
'''

import hamming
import distribution
from sys import argv


def efficiency(data_size, num_transmissions, message_len):
    return data_size / (num_transmissions * message_len)


#def average_efficiency(efficiencies: list):
def average_efficiency(efficiencies):
    return sum(efficiencies) / len(efficiencies)


def simulate(num_simulations, error_rate, message_len, k):
    efficiencies = []
    for _ in range(num_simulations):
        num_errors = distribution.num_errors(message_len, error_rate)
        bound = hamming.hamming_bound(message_len, k)

        num_transmissions = 1
        while num_errors > bound:
            num_errors = distribution.num_errors(message_len, error_rate)
            bound = hamming.hamming_bound(message_len, k)
            num_transmissions += 1

        efficiencies.append(efficiency(k, num_transmissions, message_len))

    return average_efficiency(efficiencies)


if __name__ == "__main__":
    '''
    Command line parameters:
        -u data size u
        -p bit error probability
        -r number of redundant bits n-k
    '''

    if len(argv) > 1:
        data_size = int(argv[argv.index("-u") + 1])
        error_rate = float(argv[argv.index("-p") + 1])
        redundant_bits = int(argv[argv.index("-r") + 1])
        k = data_size + 100   # 100 is overhead
        packet_size = k + redundant_bits   # encoding process

    else:   # interactive mode
        data_size = int(input("Data size (int): "))
        error_rate = float(input("Independent bit probability error (float): "))
        redundant_bits = int(input("Redundant bit size (int):"))
        k = data_size + 100   # 100 is overhead
        packet_size = k + redundant_bits   # encoding process

    print(data_size, error_rate, redundant_bits)

    num_simulations = 10 ** 6
    simulate(num_simulations, error_rate, packet_size, k)
