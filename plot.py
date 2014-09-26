'''
Plotting utility for COSC263 Assignment.

Plots p on the x-axis and average efficency on the y-axis.
'''

import matplotlib.pyplot as plt
import math 


import bsc_simulation
import two_state_simulation

YLABEL = "Average efficiency"
XLABEL = "p"


def plot_simulation(p, efficiencies, p2 = None, efficiencies2 = None):
    if p2 == None and efficiencies2 == None:
        # Draw graph
        plt.plot(p, efficiencies)

        # Label Axis
        plt.ylabel(YLABEL)
        plt.xlabel(XLABEL)

        plt.show()
    else:
        # Draw graph
        plt.plot(p, efficiencies)
        plt.plot(p2, efficiencies2)

        # Label Axis
        plt.ylabel(YLABEL)
        plt.xlabel(XLABEL)

        plt.show()


if __name__ == "__main__":

    '''
    TODO: Read input from command line to get parameters
    '''

    # Q3 | BSC, where p = 0.001 and p = 0.01
    p_ten = 0.01; p_ten_container = []
    p_hund = 0.001; p_hund_container = []

    for user_data in range(100, 200, 10):
        # number of checkbits is 10% of packetsize
        n = user_data + 100
        check_bits = math.ceil(.1 * n)   
        k = n + check_bits
        p_ten_container.append([user_data,
            bsc_simulation.simulate(10**6, p_ten, user_data, (check_bits + 100 + user_data))])
        
        p_hund_container.append([user_data,
            bsc_simulation.simulate(10**6, p_hund, user_data, (check_bits + 100 + user_data))])
    
    plot_simulation(p_ten_container[0], p_ten_container[1], p_hund_container[0], p_hund_container[1])

    # Q4 | Plot BSC with varying effs
    """
    u = 512
    p_min = 0.0001
    p_max = 0.01
    p_step = 0.0002
    num_sims = 10 ** 6

    (p, efficiencies) = bsc_simulation.prob_sim(p_min, p_max, p_step, num_sims, u)
    printf("Finished BSC Simulation")
    plot_simulation(p, efficiencies)
    """

    # Q5 | Two State Simulation
    """
    pg = (10)**(-3)
    pb = (1.99)*(10**-2)
    user_data = 1024
    two_state_efficiencies = []
    bsc_efficiencies = []
    for check_bits in range(0, 500, 10):
        two_state_efficiencies.append([check_bits, two_state_simulation.simulate(10**6, pg, pb, user_data, (check_bits + 100 + user_data))])
        print('Finished two state')
        #bsc_efficiencies.append([check_bits,
        #    bsc_simulation.simulate(10**6, 10**-3, user_data, (check_bits + 100 + user_data))])
        #print("Finished Bsc")

    plot_simulation(two_state_efficiencies[0], two_state_efficiencies[1])
    """
