'''
Plotting utility for COSC263 Assignment.

Plots p on the x-axis and average efficency on the y-axis.
'''

import matplotlib.pyplot as plt


import bsc_simulation
import two_state_simulation

YLABEL = "Average efficiency"
XLABEL = "p"


def plot_simulation(p, efficiencies):

    # Draw graph
    plt.plot(p, efficiencies)

    # Label Axis
    plt.ylabel(YLABEL)
    plt.xlabel(XLABEL)

    plt.show()


if __name__ == "__main__":

    '''
    TODO: Read input from command line to get parameters
    '''

    # Question 4
    # Plot BSC with varying effs
#    u = 512
#    p_min = 0.0001
#    p_max = 0.01
#    p_step = 0.0002
#    num_sims = 10 ** 6
#
#    (p, efficiencies) = bsc_simulation.prob_sim(p_min, p_max, p_step, num_sims, u)
#    printf("Finished BSC Simulation")
#    plot_simulation(p, efficiencies)


    # Q5 | Two State Simulation
    pg = (10)**(-3)
    pb = (1.99)*(10**-2)
    user_data = 1024
    two_state_efficiencies = []
    bsc_efficiencies = []
    for check_bits in range(0, 50, 10):
        two_state_efficiencies.append([check_bits, two_state_simulation.simulate(10**6, pg, pb, user_data, (check_bits + 100 + user_data))])
        print('Finished two state')
        #bsc_efficiencies.append([check_bits,
        #    bsc_simulation.simulate(10**6, 10**-3, user_data, (check_bits + 100 + user_data))])
        #print("Finished Bsc")


    plot_simulation(two_state_efficiencies[0], two_state_efficiencies[1])


