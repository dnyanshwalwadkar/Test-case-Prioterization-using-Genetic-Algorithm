__author__ = 'David T. Pocock'

import timeit
from operator import itemgetter
from genetic_algorithm import GeneticAlgorithm


class RandomSearch(GeneticAlgorithm):
    show_each_solution = None
    silent = None
    mean_time = None
    mean_fitness = None
    fitness_values = None

    def __init__(self, test_case_fault_matrix, solution_size, solutions_pool_size, number_of_rounds):
        self.test_case_fault_matrix = test_case_fault_matrix
        self.solution_size = solution_size
        self.solutions_pool_size = solutions_pool_size
        self.number_of_rounds = number_of_rounds

    def run(self, number_of_runs):
        times = []
        self.fitness_values = []
        for i in range(0, number_of_runs):
            start_time = timeit.default_timer()
            solutions = self.generate_population(self.solutions_pool_size, self.solution_size)
            best_solution = self.evaluate(solutions)
            round_number = 0
            if not self.silent:
                if self.show_each_solution is True:
                    print("\n     Fitness              Solution            Round\n")
                print("Solution with fittest APFD:                {0:.10f}".format(best_solution[1]),
                      "      ", [i[0] for i in best_solution[0]])
            for i in range(0, self.number_of_rounds):
                round_number += 1
                if best_solution[1] == 1:
                    break
                new_solutions = self.generate_population(self.solutions_pool_size, self.solution_size)
                new_best_solution = self.evaluate(new_solutions)
                if self.show_each_solution:
                    print("       {}              {}            {}".
                          format(best_solution[1], [i[0] for i in best_solution[0]], str(round_number).rjust(2)))
                if new_best_solution[1] > best_solution[1]:
                    best_solution = new_best_solution
                    if not self.silent:
                        print("\nSolution with fitter APFD found:           {0:.10f}        ".format(best_solution[1]),
                              [i[0] for i in best_solution[0]])
            exec_time = timeit.default_timer() - start_time
            times.append(exec_time)
            self.fitness_values.append(best_solution[1])
            print("\nRandom search complete      Execution Time: {0:.3f} seconds".format(exec_time),
                  "          Fittest APFD value found:", best_solution[1], "          Rounds:", round_number, "\n")
        self.set_stats(times, self.fitness_values, number_of_runs)

    def evaluate(self, solutions):
        solutions_evaluated = []
        for solution in solutions:
            solution_fitness = self.fitness(solution, self.solution_size)
            solution = solution, solution_fitness
            solutions_evaluated.append(solution)
        best_solution = max(solutions_evaluated, key=itemgetter(1))
        return best_solution

    def set_show_each_solution(self, boolean):
        self.show_each_solution = boolean

    def set_silent(self, boolean):
        self.silent = boolean

    def set_stats(self, times, fitness_values, number_of_runs):
        self.mean_time = sum(times) / number_of_runs
        self.mean_fitness = sum(fitness_values) / number_of_runs
        return self.mean_time
    def exe(self):
         return self.mean_time

    def get_stats(self):
        print("\n\nRandom search run           Mean Execution Time: {0:.3f} seconds".format(self.mean_time)
                  , "         Mean Fitness (APFD):", self.mean_fitness, "\n\n\n")
        return self.fitness_values
