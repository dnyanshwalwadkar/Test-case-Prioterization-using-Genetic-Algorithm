import numpy as np
import random, string, timeit


class WhaleOptimization():
    """class implements the whale optimization algorithm as found at
    http://www.alimirjalili.com/WOA.html
    and
    https://doi.org/10.1016/j.advengsoft.2016.01.008
    """

    def __init__(self, test_case_fault_matrix, constraints, nsols, b, a, maximize=False):
        self.test_case_fault_matrix = test_case_fault_matrix
        #self._constraints = constraints
        # self._sols = self._init_solutions(nsols)
        self._b = b
        self._a = a
        #self._a_step = a_step
        self._maximize = maximize
        self._best_solutions = []
        self.population_size = 1000
        self.chromosome_size = 23


    # def get_solutions(self):
    #     """return solutions"""
    #     return self._sols

    def optimize(self):
        """solutions randomly encircle, search or attack"""

        population = self.generate_population(self.population_size, self.chromosome_size)
        counter = 0
        fitness = {}
        for chromosome in population:
            counter += 1
            fitness_value = self.fitness(chromosome, self.chromosome_size)
            if counter == 1:
                fittest_chromosome = fitness_value
                fitness = fittest_chromosome

        ranked_sol = fitness

        #hdhdkdhfdf
        best_sol = ranked_sol
        # include best solution in next generation solutions
        new_sols = [best_sol]

        #for s in ranked_sol:
        s=ranked_sol
        if np.random.uniform(0.0, 1.0) > 0.5:
                A = self._compute_A()
                #print("---- A Value ---- ")
                #print(A)
                norm_A = np.linalg.norm(A)
                #print("norm_a--------")
                #print(norm_A)
                if norm_A < 1.0:
                    new_s = self._encircle(s, best_sol, A)
                else:
                    ###select random sol
                    random_sol = self._sols
                    new_s = self._search(s, random_sol, A)
        else:
            #print(s)
            print("---- best ----")
            print(best_sol)
            ew_s = self._attack(s, best_sol)
            #new_sols.append(self._constrain_solution(new_s))

        self._sols = np.stack(new_sols)
        #self._a -= self._a_step

    # def _init_solutions(self, nsols):
    #     """initialize solutions uniform randomly in space"""
    #     sols = []
    #     for c in self._constraints:
    #         sols.append(np.random.uniform(c[0], c[1], size=nsols))
    #
    #     sols = np.stack(sols, axis=-1)
    #     return sols

    def _constrain_solution(self, sol):
        """ensure solutions are valid wrt to constraints"""
        constrain_s = []
        for c, s in zip(self._constraints, sol):
            if c > s:
                s = c[0]
            elif c[1] < s:
                s = c[1]
            constrain_s.append(s)
        return constrain_s
    def fitness(self, chromosome, chromosome_size):
        weight = 0
        number_of_test_cases_in_set = chromosome_size
        number_of_faults = len(chromosome[0][1])
        #print(number_of_faults)

        for i in range(0, number_of_faults):
            for j in range(0, number_of_test_cases_in_set):
                #print(chromosome[j][1][i])
                if chromosome[j][1][i]:
                    weight += j+1
                   # print("1stst weight" )
                    #print(weight)
                    break
                if j == chromosome_size - 1:
                    #print(" 2nd weight")
                    #print(weight)
                    weight += number_of_test_cases_in_set + 1
        apfd = 1 - (weight/(number_of_faults * number_of_test_cases_in_set)) + 1/(2 * number_of_test_cases_in_set)

        return apfd

    def generate_population(self, population_size, chromosome_size):
        population = []
        for i in range(0, population_size):
            chromosome = []
            for j in range(0, chromosome_size):
                self.populate(j, chromosome)

            population.append(chromosome)
        return population
    def populate(self, j, chromosome):
        random_index = random.randint(0, len(self.test_case_fault_matrix) - 1)
        chromosome.append(self.test_case_fault_matrix[random_index])

        if j > 0:
            if self.check_for_duplicate(chromosome):

                chromosome.pop()
                self.populate(j, chromosome)

    def check_for_duplicate(self, chromosome):
        duplicate_checker = []
        for test_case, faults in chromosome:
            duplicate_checker.append(test_case)
        return len(duplicate_checker) != len(set(duplicate_checker))

    @property
    def _rank_solutions(self):
        """find best solution"""
        #fitness = self._opt_func(self._sols[:, 0], self._sols[:, 1])
        #print("@#$%##")
        #self._sols = self._sols[:, 0], self._sols[:, 1]
        population = self.generate_population(self.population_size ,self.chromosome_size)
        counter = 0
        fitness = {}
        for chromosome in population:
            counter += 1
            fitness_value = self.fitness(chromosome, self.chromosome_size)
            if counter == 1:
                fittest_chromosome =  fitness_value
                fitness = fittest_chromosome

            #if fitness_value >= fittest_chromosome[1]:
             #   fittest_chromosome =  fitness_value
              #  if fitness_value == 1:
               #     break
        #fitness = {}
        #fitness=fittest_chromosome
        print("fitness value----")
        print(fitness)
        #sol_fitness = self.fitness, self._sols

        #sol_fitness = [(f) for f in zip(fitness)]


        #sol_fitness = [(f, s) for f, s in zip(fitness, self._sols)]
        #print("------sol fitness-----")
        #print(sol_fitness)

        # best solution is at the front of the list
        #sol_fitness=sorted(sol_fitness,key=None, reverse=False)
        #ranked_sol = sol_fitness
        #self._best_solutions.append(ranked_sol[0])

        #ranked_sol = list(sorted(sol_fitness, key=lambda x: x[0], reverse=self._maximize))
        #ranked_sol=list(sorted(fitness),key=lambda x: x[0], reverse=self._maximize)
        self._best_solutions.append(fitness)
        #print("_best_solutions.append(fitness)")
        #print(self._best_solutions)

        return fitness
        #return  ranked_sol

    def print_best_solutions(self):
        # print('generation best solution history')
        # print('([fitness], [solution])')
        # for s in self._best_solutions:
        #     print(s)
        print('\n')
        print('best solution')
        print('([fitness])')
        print(sorted(self._best_solutions))
        #print(self._maximize)

    def _compute_A(self):
        r = np.random.uniform(0.0, 1.0, size=2)
        return (2.0 * np.multiply(self._a, r)) - self._a

    def _compute_C(self):
        return 2.0 * np.random.uniform(0.0, 1.0, size=2)

    def _encircle(self, sol, best_sol, A):
        D = self._encircle_D(sol, best_sol)
        return best_sol - np.multiply(A, D)

    def _encircle_D(self, sol, best_sol):
        C = self._compute_C()
        np.multiply(C, best_sol)
        D = np.linalg.norm(np.multiply(C, best_sol) - sol)
        return D

    def _search(self, sol, rand_sol, A):
        D = self._search_D(sol, rand_sol)
        return rand_sol - np.multiply(A, D)

    def _search_D(self, sol, rand_sol):
        C = self._compute_C()
        print(C)
        print(rand_sol)
        print(np.multiply(C[0], rand_sol[0:1]))
        return np.linalg.norm(np.multiply(C, rand_sol) - sol)

    def _attack(self, sol, best_sol):
        print("best solution")
        print(best_sol)
        print("solutions")
        self._best_solutions=best_sol
        print(sol)
        D = np.linalg.norm(best_sol - sol)
        L = np.random.uniform(-1.0, 1.0, size=2)
        return np.multiply(np.multiply(D, np.exp(self._b * L)), np.cos(2.0 * np.pi * L)) + best_sol