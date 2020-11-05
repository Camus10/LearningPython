# multinomial distribution is a generalisation of binomial distribution
# it desribes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two
# example : blood type population, dice roll outcome
# n     - number of possible outcomes
# pvals - list of probabilities of outcomes
# size  - the shape of returned array

from numpy import random

# chance of dice
x = random.multinomial(n = 6, pvals = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)