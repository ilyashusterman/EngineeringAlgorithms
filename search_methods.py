from unittest import TestCase


def linear_search(sequence, target):
    # value_found = filter(lambda x: x == target, sequence)
    for index, item in enumerate(sequence):
        if item == target:
            return index
    indexes = [index for value, index in zip(sequence, range(len(sequence)))
               if value == target][0]
    if len(indexes) is 0:
        return None
    else:
        return indexes[0]


def binary_search(sorted_collection, item):
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = (left + right) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        else:
            if item < current_item:
                right = midpoint - 1
            else:
                left = midpoint + 1

    return None


class TestSearchAlgorithms(TestCase):

    def test_linear_search(self):
        value_found = linear_search([0, 5, 7, 10, 15], 0)
        self.assertEqual(value_found, 0)
        value_found = linear_search([0, 5, 7, 10, 15], 5)
        self.assertEqual(value_found, 1)

    def test_binary_search(self):
        pass

if __name__ == '__main__':
    print('Using linear search:={}'.format(
        linear_search([0, 5, 7, 10, 15], 0)))
