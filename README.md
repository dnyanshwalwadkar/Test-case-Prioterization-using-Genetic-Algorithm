# Test-case-Prioterization-using-Genetic-Algorithm
Prioritize test case scenarios by identifying the critical path cluster using Genetic algorithm

Sotware testing involves identifying the test cases which discovers errors in the program . However , exhaustive testing of
sotware is very time consuming. In this project we are prioritizing test case scenarios by identifying the critical path clusters 
using genetic algorithm.

# Method
The test case scenarios are deliverd from the UML activity diagram and state chart digram.
Tesing efficiency is optimized by applying the genetic algorithm on the test data.

# Genetic Algorithm
A GA uses three operators on its population which are described below

1. Selection 
2. Crossover or Recombination
3. Mutation

 # Selection :-
 A selection scheme is applied to determine how individuals are chosen for mating based on their
fitness. Fitness can be defined as a capability of an individual to survive and reproduce in an
environment. Selection generates the new population from the old one, thus starting a new generation. Each
chromosome is evaluated in present generation to determine its fitness value. This fitness value is used
to select the better chromosomes from the population for the next generation.
 
# Crossover or Recombination :-
After selection, the crossover operation is applied to the selected chromosomes. It involves swapping of genes or
sequence of bits in the string between two individuals. This process is repeated with different parent
individuals until the next generation has enough individuals. After crossover, the mutation operator is
applied to a randomly selected subset of the population.

# Mutation :-
Mutation alters chromosomes in small ways to introduce new good traits. It is applied to
bring diversity in the population.

