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


def get_state(previous_state_good):

    new_state = None

    p_gg = 0.9
    p_bb = 0.9

    # Gen random number
    random_number = numpy.random.uniform()  # q


    if previous_state_good:
        if random_number >= p_gg:
            new_state = False

    elif not previous_state_good:
        if random_number >= p_bb:
            new_state = True

    if new_state is not None:
        return new_state
    else:
        return previous_state_good


def get_error_rate(current_state_good, error_rate_g, error_rate_b):

    if current_state_good:
        error_rate = error_rate_g
    else:
        error_rate = error_rate_b

    return error_rate


def simulate(num_simulations, error_rate_g, error_rate_b,
             user_data, redundant_bits):

    k = user_data + 100
    message_len = k + redundant_bits

    efficiencies = []
    total_submissions = 0

    previous_state_good = False  # arbitarily defined, n-1 state
    error_rate = error_rate_g
    bound = hamming.hamming_bound(message_len, k)

    run = 1
    runs = []

    for _ in range(num_simulations):

        # Send initial packet
        num_errors = distribution.num_errors(message_len, error_rate)

        # Update channel state
        current_state_good = get_state(previous_state_good)
        error_rate = get_error_rate(current_state_good,
                                    error_rate_g, error_rate_b)
        if current_state_good == previous_state_good:
            run += 1
        else:
            runs.append(run)
            run = 1

        previous_state_good = current_state_good

        # Resend until all errors can be corrected
        num_transmissions = 1
        while num_errors > bound:
            num_errors = distribution.num_errors(message_len, error_rate)
            num_transmissions += 1

            # Update channel state
            current_state_good = get_state(previous_state_good)
            error_rate = get_error_rate(current_state_good,
                                        error_rate_g, error_rate_b)

            if current_state_good == previous_state_good:
                run += 1
            else:
                runs.append(run)
                run = 1

            previous_state_good = current_state_good

        efficiencies.append(efficiency(user_data,
                                       num_transmissions, message_len))
        total_submissions += num_transmissions

    print(numpy.average(runs))
#    print(total_submissions)
    return numpy.average(efficiencies)


if __name__ == "__main__":
    '''
    Command line parameters:
        -u data size u
        -pg bit error probability (good)
        -pb bit error probability (bad)
        -r number of redundant bits n-k
    '''
    overhead = 100
    num_simulations = 10
    # Get simulation Parameters
    if len(argv) > 1:
        user_data = int(argv[argv.index("-u") + 1])
        error_rate_g = float(argv[argv.index("-pg") + 1])
        error_rate_b = float(argv[argv.index("-pg") + 1])
        redundant_bits = int(argv[argv.index("-r") + 1])

        print(average_efficiency)
