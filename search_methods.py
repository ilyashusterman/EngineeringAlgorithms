from unittest import TestCase


def linear_search(sequence, target):
    """Algorithm 	Best case 	Expected 	Worst case"""
    """Linear search 	O(1) 	O(N) 	O(N)"""
    for index, item in enumerate(sequence):
        if item == target:
            return index
    indexes = [index for value, index in zip(sequence, range(len(sequence)))
               if value == target][0]
    if len(indexes) is 0:
        return None
    else:
        return indexes[0]
    # value_found = filter(lambda x: x == target, sequence)
    # Second slower option


def binary_search(sorted_collection, search_value):
    """Algorithm 	Best case 	Expected 	Worst case"""
    """Binary search 	O(1) 	O(log N) 	O(log N)"""
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = (left + right) // 2
        current_value = sorted_collection[midpoint]
        if current_value == search_value:
            return midpoint
        else:

            if search_value < current_value:
                right = midpoint - 1
            else:
                left = midpoint + 1

    return None


class TestSearchAlgorithms(TestCase):

    def test_linear_search(self):
        index_found = linear_search([0, 5, 7, 10, 15], 0)
        self.assertEqual(index_found, 0)
        index_found = linear_search([0, 5, 7, 10, 15], 5)
        self.assertEqual(index_found, 1)

    def test_binary_search(self):
        index_found = binary_search([0, 5, 7, 10, 15], 15)
        self.assertEqual(index_found, 4)
        none_value =  binary_search([0, 5, 7, 10, 15], 6)
        self.assertIsNone(none_value)