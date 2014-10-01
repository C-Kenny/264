 #!/usr/bin/python3

'''
Authors:    Dillon George and Carl Kenny
Program:    Plots p on the x-axis and average efficency on the y-axis.
'''

import matplotlib.pyplot as plt
from numpy import ceil
from sys import argv

import bsc_simulation
import two_state_simulation

def plot_simulation(x1, y1, dest_name, xlabel, ylabel, x2=None, y2=None,
                    line1_label=None, line2_label=None):
    """ Plots simulation, the second line (x2, y2) is optional """

    # Label axes
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)



    if x2 is None and y2 is None:
        # Draw single line graph
        line1, = plt.plot(x1, y1)

    else:
        # Draw multi-line graph
        line1, = plt.plot(x1, y1)
        line2, = plt.plot(x2, y2)

    if line1_label is not None and line2_label is not None:
        plt.legend([line1, line2], [line1_label, line2_label])

    plt.savefig(dest_name)
    plt.close()


def question_three():
    """ Q3 | BSC, where p = 0.001 and p = 0.01 """
    p_ten = 0.01
    p_ten_container = []
    p_hund = 0.001
    p_hund_container = []

    user_data = range(100, 2010, 10)

    for data in user_data:
        # number of checkbits is 10% of packetsize
        n = data + 100
        check_bits = ceil(.1 * n)
        k = n + check_bits
        p_ten_container.append(
            bsc_simulation.simulate(10**6, p_ten, data, check_bits))

    for data in user_data:
        print("plotting 100s")
        n = data + 100
        check_bits = ceil(.1 * n)
        k = n + check_bits
        p_hund_container.append(
            bsc_simulation.simulate(10**6, p_hund, data, check_bits))

    plot_simulation(user_data, p_ten_container,
                    dest_name="img/q3.png", xlabel="u", ylabel="Average Efficiency",
                    line1_label="p=0.01", line2_label="p=0.001",
                    x2=user_data, y2=p_hund_container)


def question_four():
    """ Q4 | Plot BSC with varying efficiencies """
    u = 512
    p_min = 0.0001
    p_max = 0.01
    p_step = 0.0002
    num_sims = 10 ** 6

    (p, efficiencies) = bsc_simulation.prob_sim(p_min, p_max, p_step, num_sims, u)
    print(p, efficiencies)
    print("Finished BSC Simulation")
    plot_simulation(p, efficiencies, dest_name="img/q4.png",
                    xlabel='p', ylabel='Average Efficiency')

def question_five():
    """ Q5 | Two State Simulation """
    pg = (10)**(-5)
    pb = (1.99)*(10**-3)
    user_data = 1024
    two_state_efficiencies = []
    bsc_efficiencies = []

    bit_range = range(0, 510, 10)
    for check_bits in bit_range:
        two_state_efficiencies.append(two_state_simulation.simulate(10**6,
                                      pg, pb, user_data, check_bits))
        bsc_efficiencies.append(bsc_simulation.simulate(10**6, 10**-3,
                                                        user_data, check_bits))

    plot_simulation(bit_range, two_state_efficiencies, x2=bit_range, 
                    y2=bsc_efficiencies, xlabel="n-k", ylabel="Average Efficiency",
                    line1_label="Two State Channel",
                    line2_label="BSC Channel", dest_name="img/q5.png")

if __name__ == "__main__":
    '''
    Command line parameters:
        -q3
        -q4
        -q5
        -all
    '''

    if len(argv) > 1:
        question = argv[1]

        if question == "-q3":
            question_three()

        elif question == "-q4":
            question_four()

        elif question == "-q5":
            question_five()

        elif question == "-all":
            question_three()
            question_four()
            question_five()

