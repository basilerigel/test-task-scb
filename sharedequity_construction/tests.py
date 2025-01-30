from sharedequity_construction.sharedequity import calculate_ratios
from collections import namedtuple

TestCase = namedtuple('TestCase', 'case expected_result')

TEST_CASES = [
    TestCase(case=[1, 1], expected_result=[0.500, 0.500]),
    TestCase(case=[1.5, 3, 6, 1.5], expected_result=[0.125, 0.250, 0.500, 0.125]),
]

# в условиях задачи написано не использовать сторонних библиотек, поэтому без pytest вот так
if __name__ == '__main__':
    for test_cases in TEST_CASES:
        assert calculate_ratios(ratios=test_cases.case) == test_cases.expected_result
