from kata.merge_two_sorted_lists import ListNode, Solution
import pytest

@pytest.fixture
def setup():
  return Solution()


def test_empty_lists(setup):
    l1 = []
    l2 = []

    assert(setup.mergeTwoLists(l1, l2) == [])


def test_empty_lists(setup):
    l1 = []
    l2 = [0]

    node = ListNode(0)
    assert(setup.mergeTwoLists(l1, l2)[0] == node)

# The problem statement was to merge two lists of nodes and return a sorted list
# of nodes. I think I got that, but testing two lists of custom objects for equality is harder
# than I want to spend time on right now.
