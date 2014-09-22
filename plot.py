'''
Plotting utility for COSC263 Assignment.

Plots p on the x-axis and average efficency on the y-axis.
'''

import matplotlib.pyplot as plt


import bsc_simulation

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

    # Plot BSC
    (p, efficiencies) = bsc_simulation.multi_sim(0.001, 0.01, 0.002, 10**6, 10, 20)
    plot_simulation(p, efficiencies)
    print(list(zip(p, efficiencies)))

