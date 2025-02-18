import random
import json
from typing import List

random.seed(10)

# Random Test Case Generation
def generate_random_test_cases(num_cases: int, list_size: int, min_val: int, max_val: int):
    test_cases = []
    for _ in range(num_cases):
        arr = [random.randint(min_val, max_val) for _ in range(list_size)]
        t = random.choice(arr)  # Target is always an element from the array
        test_cases.append({"arr": arr, "t": t})
        test_cases.append({"arr": arr, "t": min_val - 1})
        test_cases.append({"arr": arr, "t": max_val + 1})

    return test_cases

# Saving Test Cases to a File
def save_test_cases_to_file(test_cases: List[dict], filename: str):
    with open(filename, 'w') as file:
        json.dump(test_cases, file)

# Example usage
random_test_cases = generate_random_test_cases(750, 5, 1, 100)  # 10 cases, 5 elements per case
save_test_cases_to_file(random_test_cases, 'random_test_cases.json')