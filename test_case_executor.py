import json
from typing import List
from types import FunctionType

import membership_std
import membership_error1
import membership_error2
import membership_error3
import membership_error4
import membership_error5
import membership_error6

# Trusted Oracle function (assumed correct implementation)
def oracle_membership(arr: List[int], t: int) -> bool:
    return t in arr

# Function under test
def membership(arr: List[int], t: int) -> int:
    try:
        if arr.index(t) != -1:
            return True
    except ValueError:
        return False

# Function to execute test cases and compare with oracle
def run_tests_with_oracle(test_file: str, result_file: str, membership: FunctionType):
    with open(test_file, 'r') as file:
        test_cases = json.load(file)

    total_tests = 0
    error_found_at = -1  # Position where first error occurs

    for idx, case in enumerate(test_cases):
        arr, t = case['arr'], case['t']
        expected = oracle_membership(arr, t)  # Get expected result from oracle
        actual = membership(arr, t)  # Run function under test

        total_tests += 1

        # Check for errors
        if actual != expected and error_found_at == -1:
            error_found_at = total_tests  # Store when first error occurs

    # If no error is found, return total test cases
    if error_found_at == -1:
        error_found_at = total_tests

    # Save results
    results = {
        "Total Tests Executed": total_tests,
        "Tests Until First Error": error_found_at
    }

    with open(result_file, 'w') as file:
        json.dump(results, file, indent=2)

    print(f"Results saved to {result_file}")

# Example usage
run_tests_with_oracle('pairwise_test_cases.json', 'N_5_test_results_pairwise.json', membership_std.membership)
run_tests_with_oracle('random_test_cases.json', 'N_5_test_results_random.json', membership_std.membership)

run_tests_with_oracle('pairwise_test_cases.json', 'N_5_test_results_pairwise_error1.json', membership_error1.membership)
run_tests_with_oracle('random_test_cases.json', 'N_5_test_results_random_error1.json', membership_error1.membership)

run_tests_with_oracle('pairwise_test_cases.json', 'N_5_test_results_pairwise_error2.json', membership_error2.membership)
run_tests_with_oracle('random_test_cases.json', 'N_5_test_results_random_error2.json', membership_error2.membership)

run_tests_with_oracle('pairwise_test_cases.json', 'N_5_test_results_pairwise_error3.json', membership_error3.membership)
run_tests_with_oracle('random_test_cases.json', 'N_5_test_results_random_error3.json', membership_error3.membership)

run_tests_with_oracle('pairwise_test_cases.json', 'N_5_test_results_pairwise_error4.json', membership_error4.membership)
run_tests_with_oracle('random_test_cases.json', 'N_5_test_results_random_error4.json', membership_error4.membership)

run_tests_with_oracle('pairwise_test_cases.json', 'N_5_test_results_pairwise_error5.json', membership_error5.membership)
run_tests_with_oracle('random_test_cases.json', 'N_5_test_results_random_error5.json', membership_error5.membership)

run_tests_with_oracle('pairwise_test_cases.json', 'N_5_test_results_pairwise_error6.json', membership_error6.membership)
run_tests_with_oracle('random_test_cases.json', 'N_5_test_results_random_error6.json', membership_error6.membership)
