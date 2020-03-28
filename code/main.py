


import hill_climbing
import random_search
#from genetic_algorithm import GeneticAlgorithm
import csv_parser

import genetic_algorithm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os.path


def main():
    runs = 5
    rounds = 1
    chromosome_size = 50
    population_size = 200
    data_set_name = 'bigfaultmatrix.txt'

    pwd = os.path.abspath(os.path.dirname(__file__))
    data_set_path = os.path.join(pwd, data_set_name)
    parser =  csv_parser.CSVParser(data_set_path)
    test_case_fault_matrix = parser.parse_data(True)
    print(test_case_fault_matrix)

    ga = genetic_algorithm.GeneticAlgorithm(test_case_fault_matrix, chromosome_size, population_size, rounds, 0.5, 0.08, 0.05, 0.75)


    ga.set_show_each_chromosome(True)
    ga.set_show_fitness_internals(True)
    ga.set_show_crossover_internals(True)
    ga.set_show_mutation_internals(True)
    ga.set_show_duplicate_internals(True)
    ga.set_silent(True)
    ga.run(runs)
    ga_fitness = ga.get_stats()
    ExeTime1 = ga.exe()



    for i in range(0, 2):
        if i == 0:
            hc = hill_climbing.HillClimbing(test_case_fault_matrix, chromosome_size, population_size, rounds, False)

        else:
            hc = hill_climbing.HillClimbing(test_case_fault_matrix, chromosome_size, population_size, rounds, True)

        hc.set_show_each_solution(True)
        hc.set_show_fitness_internals(True)
        hc.set_show_swapping_internals(True)
        hc.set_silent(True)
        hc.run(runs)
        if i==0:
            ExeTime2 = hc.exe()
        else:
            ExeTime3 = hc.exe()


        if i == 0: hc_internal_fitness = hc.get_stats()
        else: hc_external_fitness = hc.get_stats()

    rs = random_search.RandomSearch(test_case_fault_matrix, chromosome_size, population_size, rounds)
    rs.set_show_each_solution(True)
    rs.set_silent(True)
    rs.run(runs)
    rs_fitness = rs.get_stats()
    ExeTime4 = rs.exe()
    print("------------------------")
    print(ExeTime1,ExeTime3,ExeTime4,ExeTime2)
    rs_data = np.array(rs_fitness)
    hs_internal = np.array(hc_internal_fitness)
    hs_external = np.array(hc_external_fitness)
    ga_data = np.array(ga_fitness)
    ga_data=ga_data.mean()
    # test_cases_per_test_suite = np.array([5, 10, 20, 23, 30, 50, 100])
    # unique_large_apfd = np.array([0.4594736842105263, 0.6063157894736844, 0.6867105263157895, 0.6978260869565216, 0.7128947368421051, 0.7326842105263159, 0.7480263157894737])
    # full_large_apfd = np.array([0.44631578947368417, 0.6023684210526316, 0.6846052631578947, 0.6958810068649884, 0.7122807017543858, 0.7320526315789474, 0.7476578947368421])

    # plt.plot(test_cases_per_test_suite, unique_large_apfd, '-gD')
    # plt.xlabel("Test Cases per Test Suite")
    # plt.ylabel("Mean Fitness (APFD)")
    # plt.xticks(np.arange(min(test_cases_per_test_suite), max(test_cases_per_test_suite) + 1, 5.0))

    ## combine these different collections into a list
    data_to_plot = [rs_data.mean(), hs_internal.mean(), hs_external.mean(), ga_data]
    print("********************************************************")
    print(data_to_plot)
    #data_to_plot = [ga_data]

    # Create a figure instance
    #
    #plt.xlabel("Runs/Delivery")
    #plt.ylabel("Frequency")
    plt.title('Algorithm comparisom')
    plt.xlabel('Algorithm')
    plt.ylabel('APFD')
    left = [1, 2, 3, 4, 5]
    tick_label = ['RS', 'HC_IS', 'HC_ES', 'GA']
    plt.bar(height=data_to_plot,x=tick_label,tick_label=tick_label,width = 0.8)
    plt.show()
    #plt.ylabel('Execution Time')
    #plt.xlabel('Different Algorithms')
    #plt.plot()

    #plt.show()

    #height = [ExeTime1, ExeTime2, ExeTime3, ExeTime4]

    #y_pos = np.arange(len(bars))

    # Create bars and choose color
    #plt.bar(y_pos, height, color=(0.5, 0.1, 0.5, 0.6))

    # Add title and axis names


    # Limits for the Y axis
    #plt.ylim(0, 60)

    # Create names
    #plt.xticks(y_pos, bars)

    #graph_path = os.path.join(pwd, 'CompGraph1.pdf')
    #pdf = PdfPages(graph_path)
    #plt.savefig(pdf, format='pdf', bbox_inches='tight')
    #plt.show()

    pdf = None

if __name__ == "__main__":
    main()
