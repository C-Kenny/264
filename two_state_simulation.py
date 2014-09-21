#!/Users/dtg/Dropbox/UC_2014/S2/264/env/bin/python

'''
Simulates a 2-State channel, modelled using a binomial distribution.
'''

import hamming
import numpy    # for uniform random numbers
import distribution
from sys import argv


def efficiency(data_size, num_transmissions, message_len):
    return data_size / (num_transmissions * message_len)


def average_efficiency(efficiencies):
    return sum(efficiencies) / len(efficiencies)


def simulate(num_simulations, error_rate_g, error_rate_b, user_data, message_len):
    efficiencies = []
    k = user_data + 100
    total_submissions = 0
    previous_state_good = True # arbitarily defined, n-1 state
    for _ in range(num_simulations):

        # Send one package
        random_number = numpy.random.uniform()  # q

        if previous_state_good == True:
            if random_number < error_rate_g:    
                error_rate = error_rate_g
            else:
                error_rate = error_rate_b
                previous_state_good = False

        else: 
            if random_number < error_rate_b:
                error_rate = error_rate_b
            else:
                error_rate = error_rate_g
                previous_state_good = True

        num_errors = distribution.num_errors(message_len, error_rate)
        bound = hamming.hamming_bound(message_len, k)

        # While not successful
        num_transmissions = 1

        while num_errors < bound:
            num_errors = distribution.num_errors(message_len, error_rate)
            num_transmissions += 1
            print("Number errors: ", num_errors)
            print("Efficiencies: ", efficiencies)
            print("Submissions ", total_submissions)


        efficiencies.append(efficiency(k, num_transmissions, message_len))
        total_submissions += num_transmissions

    print(total_submissions)
    return average_efficiency(efficiencies)

def interactiveMode():
    """ Gets required data from standard input. """

    print(">>> Two-State Channel Simulation")
    user_data = int(input("Data size (int): "))
    print("You will now be asked to enter the probabilities for a 'good' & 'bad' state, please make pb >> pg")
    error_rate_g = float(input("Independent bit probability error (pg): "))
    error_rate_b = float(input("Independent bit probability error (pb): "))
    if error_rate_g > error_rate_b:
        print("Invalid bit probability rates. pb must be larger than pg\n--RESTARTING NOW--\n")
        interactiveMode()

    redundant_bits = int(input("Redundant bit size (int):"))

    return user_data, error_rate_g, error_rate_b, redundant_bits

if __name__ == "__main__":
    '''
    Command line parameters:
        -u data size u
        -pg bit error probability (good)
        -pb bit error probability (bad)
        -r number of redundant bits n-k
    '''
    overhead = 100
    num_simulations = 10 ** 2

    # Get simulation Parameters
    if len(argv) > 1:
        user_data = int(argv[argv.index("-u") + 1])
        error_rate_g = float(argv[argv.index("-pg") + 1])
        error_rate_b = float(argv[argv.index("-pg") + 1])
        redundant_bits = int(argv[argv.index("-r") + 1])

    else:   # Interactive Mode
        user_data, error_rate_g, error_rate_b, redundant_bits = interactiveMode()

    message_len = user_data + overhead + redundant_bits

    average_efficiency = simulate(num_simulations, error_rate_g,error_rate_b,
                                  user_data, message_len)

    print(average_efficiency)
