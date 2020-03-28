


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

    rounds = 5
    chromosome_size = 23
    population_size = 1000
    data_set_name = 'bigfaultmatrix4.txt'

    pwd = os.path.abspath(os.path.dirname(__file__))
    data_set_path = os.path.join(pwd, data_set_name)
    parser =  csv_parser.CSVParser(data_set_path)
    test_case_fault_matrix = parser.parse_data(True)
    print(test_case_fault_matrix)

    ga = genetic_algorithm.GeneticAlgorithm(test_case_fault_matrix, chromosome_size, population_size, rounds, 0.8, 0.15, 0.05, 0.75)

    ga.set_show_each_chromosome(False)
    ga.set_show_fitness_internals(False)
    ga.set_show_crossover_internals(False)
    ga.set_show_mutation_internals(False)
    ga.set_show_duplicate_internals(False)
    ga.set_silent(False)
    runs = 5
    ga.run(runs)

    #print("------------- Execution time ----------- ")
    ExeTime1=ga.exe()
    ga_fitness1 = ga.get_stats()

    print("------------- New Mutation  rate -------------")

    ga = genetic_algorithm.GeneticAlgorithm(test_case_fault_matrix, chromosome_size, population_size, rounds,  0.8, 0.15,
                                            0.05, 0.75)

    ga.set_show_each_chromosome(False)
    ga.set_show_fitness_internals(False)
    ga.set_show_crossover_internals(False)
    ga.set_show_mutation_internals(False)
    ga.set_show_duplicate_internals(False)
    ga.set_silent(False)
    runs = 10
    ga.run(runs)
    ExeTime2 = ga.exe()
    print("------------- Execution time ----------- ")
    print(ExeTime2)
    ga_fitness2 = ga.get_stats()

    print("------------- New Mutation rate -------------")

    ga = genetic_algorithm.GeneticAlgorithm(test_case_fault_matrix, chromosome_size, population_size, rounds,  0.8, 0.15,
                                            0.05, 0.75)

    ga.set_show_each_chromosome(False)
    ga.set_show_fitness_internals(False)
    ga.set_show_crossover_internals(False)
    ga.set_show_mutation_internals(False)
    ga.set_show_duplicate_internals(False)
    ga.set_silent(False)
    runs = 15
    ga.run(runs)
    ExeTime3 = ga.exe()
    print("------------- Execution time ----------- ")
    print(ExeTime3)
    ga_fitness3 = ga.get_stats()

    print("------------- New Mutation rate -------------")
    ga = genetic_algorithm.GeneticAlgorithm(test_case_fault_matrix, chromosome_size, population_size, rounds,  0.8, 0.15,
                                            0.05, 0.75)

    if __name__ == '__main__':
     ga.set_show_each_chromosome(False)
    ga.set_show_fitness_internals(False)
    ga.set_show_crossover_internals(False)
    ga.set_show_mutation_internals(False)
    ga.set_show_duplicate_internals(False)
    ga.set_silent(False)
    runs = 20
    ga.run(runs)
    ExeTime4 = ga.exe()
    ga_fitness4 = ga.get_stats()



    # test_cases_per_test_suite = np.array([5, 10, 20, 23, 30, 50, 100])
    # unique_large_apfd = np.array([0.4594736842105263, 0.6063157894736844, 0.6867105263157895, 0.6978260869565216, 0.7128947368421051, 0.7326842105263159, 0.7480263157894737])
    # full_large_apfd = np.array([0.44631578947368417, 0.6023684210526316, 0.6846052631578947, 0.6958810068649884, 0.7122807017543858, 0.7320526315789474, 0.7476578947368421])

    # plt.plot(test_cases_per_test_suite, unique_large_apfd, '-gD')
    # plt.xlabel("Test Cases per Test Suite")
    # plt.ylabel("Mean Fitness (APFD)")
    # plt.xticks(np.arange(min(test_cases_per_test_suite), max(test_cases_per_test_suite) + 1, 5.0))
    ga_data1 = np.array(ga_fitness1)
    ga_data2 = np.array(ga_fitness2)
    ga_data3 = np.array(ga_fitness3)
    ga_data4 = np.array(ga_fitness4)
    ## combine these different collections into a list
    data_to_plot = [ ga_data1,ga_data2,ga_data3,ga_data4]
    #data_to_plot = [ga_data]

    # Create a figure instance
    fig = plt.figure(1, figsize=(9, 6))

    # Create an axes instance
    ax = fig.add_subplot(111)

    ## add patch_artist=True option to ax.boxplot()
    bp = ax.boxplot(data_to_plot, patch_artist=True)

    ## change outline color, fill color and linewidth of the boxes
    for box in bp['boxes']:
        # change outline color
        box.set(color='#7570b3', linewidth=2)
        # change fill color
        box.set(facecolor='#1b9e77')

    ## change color and linewidth of the whiskers
    for whisker in bp['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)

    ## change color and linewidth of the caps
    for cap in bp['caps']:
        cap.set(color='#7570b3', linewidth=2)

    ## change color and linewidth of the medians
    for median in bp['medians']:
        median.set(color='#b2df8a', linewidth=2)

    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)

    ## Custom x-axis labels
    ax.set_xticklabels([ 'Gen 5','Gen 10','Gen 15','Gen 20'])
    plt.title("GA Diff Genrations Comaparison")
    plt.ylabel('APFD')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    # Save the figure
    graph_path = os.path.join(pwd, 'Ggraph4.pdf')
    pdf = PdfPages(graph_path)

    plt.savefig(pdf, format='pdf', bbox_inches='tight' )
    plt.show()
    pdf.close()


    #height = [ExeTime1, ExeTime2, ExeTime3, ExeTime4]
    #bars = ('Ga', 'HC1', 'HC2', 'Rs')
    #y_pos = np.arange(len(bars))

    # Create bars and choose color
    #plt.bar(y_pos, height, color=(0.5, 0.1, 0.5, 0.6))

    # Add title and axis names
    #plt.title('Different Genrations comparisom')
    #plt.xlabel('Genetic Algorithm')
    #plt.ylabel('Execution Time')

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
