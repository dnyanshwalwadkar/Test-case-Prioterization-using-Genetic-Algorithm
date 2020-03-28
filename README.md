# Test-case-Prioterization-using-Genetic-Algorithm
Prioritize test case scenarios by identifying the critical path cluster using Genetic algorithm

Sotware testing involves identifying the test cases which discovers errors in the program . However , exhaustive testing of
sotware is very time consuming. In this project we are prioritizing test case scenarios by identifying the critical path clusters 
using genetic algorithm.

we also compared the following algorithm results with genetic algortihm results and plotted graphs which you can see in one of foleder in repository
1. Hill climbing 
    i] Internal Swap
    ii] Exeternal Swap
2. Random Search
3. Whale Optimisation


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



# Whale Optimisation Algorithm
meta-heuristic optimization algorithm, called Whale Opti- mization Algorithm (WOA), which mimics the social behavior of humpback whales. The algorithm is in- spired by the bubble-net hunting strategy. WOA is tested with 29 mathematical optimization problems and 6 structural design problems. Optimization results prove that the WOA algorithm is very competi- tive compared to the state-of-art meta-heuristic algorithms as well as conventional methods. The source codes of the WOA algorithm are publicly available at http://www.alimirjalili.com/WOA.html



