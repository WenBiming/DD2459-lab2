import json
from typing import List, Tuple
import itertools

# Default values for the list
DEFAULT_ARR = [1, 2, 3, 4, 5]

# Possible values for list elements and target `t`
NON_DEFAULT_VALUES = [0, 10, 20, 30, 40]  # Different values for testing

# Generate pairwise test cases
def generate_pairwise_test_cases() -> List[dict]:
    test_cases = []
    
    # Iterate over all pairs of positions in the array
    for (i, j) in itertools.combinations(range(len(DEFAULT_ARR)), 2):
        for val1, val2 in itertools.product(NON_DEFAULT_VALUES, repeat=2):
            arr = DEFAULT_ARR[:]  # Copy default array
            arr[i], arr[j] = val1, val2  # Toggle two elements
            
            # Define multiple targets: one inside the array, one outside
            #test_cases.append({"arr": arr, "t": val1})  # Target is one of the changed values
            #test_cases.append({"arr": arr, "t": val2})
            #test_cases.append({"arr": arr, "t": -1})   # Target is not in the array
            test_cases.append({"arr": arr[1:], "t": arr[0]})   # Target is not in the array

    
    return test_cases

# Save pairwise test cases to a file
def save_pairwise_test_cases_to_file(test_cases: List[dict], filename: str):
    with open(filename, 'w') as file:
        json.dump(test_cases, file, indent=2)

# Example usage
pairwise_test_cases = generate_pairwise_test_cases()
save_pairwise_test_cases_to_file(pairwise_test_cases, 'pairwise_test_cases.json')