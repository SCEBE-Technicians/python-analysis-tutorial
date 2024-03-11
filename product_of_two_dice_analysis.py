import sys
import random
import statistics

n_sides = int(sys.argv[1])
n_trials = int(sys.argv[2])

first_die_outcomes = []
second_die_outcomes = []

for i in range(n_trials):
    first_die_outcomes.append(random.randint(1, n_sides))
    second_die_outcomes.append(random.randint(1, n_sides))
    
products = [a * b for a, b in zip(first_die_outcomes, second_die_outcomes)]

output = (f"------------------------------------------------\n"
          f"Product of two {n_sides} sided dice. {n_trials} trials\n"
          f"------------------------------------------------\n"
          f"Mean: {statistics.mean(products)}\n"
          f"Median: {statistics.median(products)}\n"
          f"Mode: {statistics.mode(products)}\n")

print(output)
