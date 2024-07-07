import numpy as np
import matplotlib.pyplot as plt
import _plotly_utils as utils


def simulate(problem_func, n_students=365, n_simulations=1000):
    # Initialize the counter of matches at 0
    matches = 0

    # Run the simulation for the desired number of times
    for _ in range(n_simulations):

        # If there is a match in the classroom add 1 to the counter of matches
        if problem_func(n_students):
            matches += 1

    # Return the ratio of number of matches / number of simulations
    return matches / n_simulations


def problem_1(n_students):
    # Predefine a specific birthday
    predef_bday = np.random.randint(0, 365)

    # Generate birthdays for every student
    gen_bdays = np.random.randint(0, 365, (n_students))

    # Check if predefined bday is among students
    return predef_bday in gen_bdays

n = 100 # try changing this value!
simulated_prob = simulate(problem_1, n_students=n, n_simulations=10_000)

print(f"The simulated probability of any student to have a bday equal to a predefined value is {simulated_prob} in a classroom with {n} students")

# Generate the simulated probability for every classroom
simulated_probs_2 = [simulate(problem_2, n_students=n) for n in utils.big_classroom_sizes]

# Create a scatterplot of simulated probabilities vs classroom size
utils.plot_simulated_probs(simulated_probs_2, utils.big_classroom_sizes)
