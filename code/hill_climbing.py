__author__ = 'David T. Pocock'

import timeit, random
from operator import itemgetter
import genetic_algorithm


class HillClimbing(genetic_algorithm.GeneticAlgorithm):
    show_each_solution = None
    show_swapping_internals = None
    silent = None
    mean_time = None
    mean_fitness = None
    climb = 0
    mean_climbs = None
    fitness_values = None

    def __init__(self, test_case_fault_matrix, solution_size, solutions_pool_size, number_of_rounds, is_external_swap):
        self.test_case_fault_matrix = test_case_fault_matrix
        self.solution_size = solution_size
        self.solutions_pool_size = solutions_pool_size
        self.number_of_rounds = number_of_rounds
        self.is_external_swap = is_external_swap

    def run(self, number_of_runs):
        times = []
        self.fitness_values = []
        number_of_climbs = []
        for i in range(0, number_of_runs):
            self.climb = 0
            start_time = timeit.default_timer()
            solutions = self.generate_population(self.solutions_pool_size, self.solution_size)
            best_solution = self.evaluate(solutions)
            round_number = 0
            if not self.silent:
                if self.show_each_solution is True:
                    print("\n     Fitness              Solution\n")
                print("Solution with fittest APFD selected:       {0:.10f}".format(best_solution[1]),
                      "                      ", [i[0] for i in best_solution[0]])
            for i in range(0, self.number_of_rounds):
                round_number += 1
                if best_solution[1] == 1:
                    break
                best_solution = self.evaluate_neighbours(best_solution, solutions, 0, self.is_external_swap)
                if self.show_each_solution:
                    print("       {}              {}            {}".
                          format(best_solution[1], [i[0] for i in best_solution[0]], str(round_number).rjust(2)))
            exec_time = timeit.default_timer() - start_time
            times.append(exec_time)
            self.fitness_values.append(best_solution[1])
            number_of_climbs.append(self.climb)
            print("\nHill Climb complete      Execution Time: {0:.3f} seconds".format(exec_time),
                  "          Fittest APFD value found:", best_solution[1], "          Climbs:", self.climb
                  , "       Rounds:", round_number, "\n")
        self.set_stats(times, self.fitness_values, number_of_climbs, number_of_runs)

    def evaluate(self, solutions):
        solutions_evaluated = []
        for solution in solutions:
            solution_fitness = self.fitness(solution, self.solution_size)
            solution = solution, solution_fitness
            solutions_evaluated.append(solution)
        best_solution = max(solutions_evaluated, key=itemgetter(1))
        return best_solution

    def evaluate_neighbours(self, best_solution, solutions, iterations, is_external_swap):
        if iterations < 200:
            if is_external_swap:
                neighbouring_solution = self.swap_externally(best_solution[0], solutions)
            else:
                neighbouring_solution = self.swap_internally(best_solution[0])
            neighbouring_solution_fitness = self.fitness(neighbouring_solution, self.solution_size)
            if neighbouring_solution_fitness > best_solution[1]:
                best_solution = neighbouring_solution, neighbouring_solution_fitness
                if not self.silent:
                    self.climb += 1

                    print("\nSolution with fitter APFD found:           {0:.10f}        ".format(best_solution[1]),
                          "Climb #{}      ".format(self.climb), [i[0] for i in best_solution[0]])
                return best_solution
            else:
                iterations += 1
                return self.evaluate_neighbours(best_solution, solutions, iterations, is_external_swap)
        else:
            return best_solution

    def swap_internally(self, solution):
        if self.show_swapping_internals: print("Solution pre-swap:   ", [i[0] for i in solution])
        first_random_index = random.randint(0, self.solution_size - 1)
        second_random_index = self.swap_test_cases(first_random_index, self.solution_size)
        solution[second_random_index], solution[first_random_index] = solution[first_random_index], solution[
            second_random_index]
        if self.show_swapping_internals:
            print("Test Case", solution[second_random_index][0], "at index #{}".format(first_random_index),
                  "swapped with Test Case", solution[first_random_index][0], "at index #{}".format(second_random_index))
            print("Solution post-swap:   ", [i[0] for i in solution], "\n")
        return solution

    def swap_externally(self, solution, solutions):
        random_picked_solution = self.find_unique_neighbour(solution, solutions)
        if self.show_swapping_internals:
            print("Solution pre-swap:       ", [i[0] for i in solution])
            print("Randomly picked solution:", [i[0] for i in random_picked_solution])
        swapped_solution = self.swap_and_check_test_cases(solution, random_picked_solution)
        if self.show_swapping_internals: print("Solution post-swap:   ", [i[0] for i in swapped_solution], "\n")
        return swapped_solution

    def find_unique_neighbour(self, solution, solutions):
        rand_solution_index = random.randint(0, len(solutions) - 1)
        random_picked_solution = solutions[rand_solution_index]
        if set([i[0] for i in random_picked_solution]) == set([i[0] for i in solution]) or len(set([i[0] for i in random_picked_solution]) - set([i[0] for i in solution])) == 0:
            if self.show_swapping_internals:
                print("Solution:                    ", [i[0] for i in solution])
                print("Randomly picked solution:    ", [i[0] for i in random_picked_solution])
                print("Failed to find unique neighbours, trying again...")
            return self.find_unique_neighbour(solution, solutions)
        else:
            return random_picked_solution

    def swap_and_check_test_cases(self, solution, random_picked_solution):
        first_random_index = random.randint(0, self.solution_size - 1)
        difference = list(set([i[0] for i in random_picked_solution]) - set([i[0] for i in solution]))
        diff_list_index = random.randint(0, len(difference) - 1)
        second_index = [i[0] for i in random_picked_solution].index(difference[diff_list_index])
        if self.show_swapping_internals:
            print("Difference in picked:", difference)
            print("Index of difference list:", diff_list_index, "elem:", difference[diff_list_index])
            print("Swap Test Case", solution[first_random_index][0], "with Test Case",
                  random_picked_solution[second_index][0])
        solution[first_random_index], random_picked_solution[second_index] = random_picked_solution[second_index], solution[first_random_index]
        if self.show_swapping_internals:
            print("Test Case", random_picked_solution[second_index][0], "at index #{}".format(first_random_index),
                      "swapped with Test Case", solution[first_random_index][0],
                      "at index #{}".format(second_index))
        return solution

    def set_show_each_solution(self, boolean):
        self.show_each_solution = boolean

    def set_silent(self, boolean):
        self.silent = boolean

    def set_show_swapping_internals(self, boolean):
        self.show_swapping_internals = boolean

    def set_stats(self, times, fitness_values, number_of_climbs, number_of_runs):
        self.mean_time = sum(times) / number_of_runs
        self.mean_fitness = sum(fitness_values) / number_of_runs
        self.mean_climbs = sum(number_of_climbs) / number_of_runs
        return  self.mean_time
    def exe(self):
         return self.mean_time

    def get_stats(self):
        print("\n\nHill Climb run complete           Mean Execution Time: {0:.3f} seconds".format(self.mean_time),
              "         Mean Fitness (APFD):", self.mean_fitness, "          Mean Climbs:", self.mean_climbs, "\n\n\n")
        return self.fitness_values
