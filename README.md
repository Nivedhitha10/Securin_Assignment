# Securin_Assignment
The Doomed Dice Challenge

assignment.py has the solution
![127 0 0 1_8080_api_roll-distribution - Google Chrome 18-12-2023 22_47_52](https://github.com/Nivedhitha10/Securin_Assignment/assets/131236071/915f3464-bec4-4077-b8b6-813fa6576598)

CODE:
import random


# Part A


die_faces = 6


# 1. Total combinations
total_combos = die_faces ** 2
print("Total combinations:", total_combos)


# 2. Distribution of sums
combinations = {}


for die1 in range(1, die_faces + 1):
    for die2 in range(1, die_faces + 1):
        sum_result = die1 + die2
        if sum_result not in combinations:
            combinations[sum_result] = 0
        combinations[sum_result] += 1


print("Distribution of sums:")
print(combinations)


# 3. Probabilities
def get_probabilities(combinations):
    probabilities = {}
    for sum_result, count in combinations.items():
        probabilities[sum_result] = count / total_combos
    return probabilities


probabilities_A = get_probabilities(combinations)
print("Probabilities A:")
print(probabilities_A)




# Part B


def undoom_dice(die_A, die_B):
    new_die_A = [2, 4, 1, 3]  # Example transformation, you can modify this based on your criteria


    new_die_B = [random.randint(1, 6) for _ in range(len(die_B))]  # Allow any number of spots <= 6


    # Shuffle new_die_A
    random.shuffle(new_die_A)


    # Shuffle new_die_B
    random.shuffle(new_die_B)


    return new_die_A, new_die_B


original_die_A = [1, 2, 3, 4, 5, 6]
original_die_B = [1, 2, 3, 4, 5, 6]


new_die_A, new_die_B = undoom_dice(original_die_A, original_die_B)


print("Original Die A:", original_die_A)
print("Original Die B:", original_die_B)
print("New Die A:", new_die_A)
print("New Die B:", new_die_B)


# 4. Probabilities after undooming
combinations_B = {}
for die_a in new_die_A:
    for die_b in new_die_B:
        sum_result = die_a + die_b
        if sum_result not in combinations_B:
            combinations_B[sum_result] = 0
        combinations_B[sum_result] += 1


probabilities_B = get_probabilities(combinations_B)
print("Probabilities B:")
print(probabilities_B)
![sum py - SECURIN - Visual Studio Code 19-12-2023 18_55_57](https://github.com/Nivedhitha10/Securin_Assignment/assets/131236071/5a706982-0cf6-44d7-b745-0564b23a8f13)


