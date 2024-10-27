import random

def swap_mutation(individual):
    """Perform swap mutation on a permutation individual."""
    # Make a copy of the individual to prevent modifying the original
    mutated_individual = individual.copy()

    # Randomly select two distinct indices
    index1, index2 = random.sample(range(len(mutated_individual)), 2)

    # Swap the elements at the selected indices
    mutated_individual[index1], mutated_individual[index2] = mutated_individual[index2], mutated_individual[index1]

    return mutated_individual

# Example usage
original_individual = [0, 1, 2, 3, 4]
mutated_individual = swap_mutation(original_individual)

print(f"Original: {original_individual}")  # Output: Original: [0, 1, 2, 3, 4]
print(f"Mutated: {mutated_individual}")    # Output could be: Mutated: [0, 2, 1, 3, 4] (order may vary)
