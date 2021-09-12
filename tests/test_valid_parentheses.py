from kata.valid_parentheses import Solution
import pytest


@pytest.fixture
def setup_solution():
    solution = Solution()

def test_single_valid_parentheses_pair(setup_solution):
    assert Solution().isValid("()")

def test_single_invalid_left_parenthesis(setup_solution):
    assert not Solution().isValid("(()")

def test_single_invalid_right_parenthesis(setup_solution):
    assert not Solution().isValid("(()")

def test_multiple_valid_parentheses(setup_solution):
    assert Solution().isValid("(([[]))]")
