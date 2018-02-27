from unittest import TestCase


def bubble_sort(bad_list):
    """Algorithm 	Best case 	Expected 	Worst case"""
    """Bubble sort 	  O(N) 	     O(N) 	        O(N^2)"""
    length = len(bad_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i + 1]:
                sorted = False
                bad_list[i], bad_list[i + 1] = bad_list[i + 1], bad_list[i]
    return bad_list


class TestSortAlgorithms(TestCase):
    def test_bubble_sort(self):
        sorted_collection = bubble_sort([0, 5, 3, 2, 2])
        self.assertEqual(sorted_collection, [0, 2, 2, 3, 5])
        sorted_collection = bubble_sort(bubble_sort([-2, -5, -45]))
        self.assertEqual(sorted_collection, [-45, -5, -2])
        sorted_collection = bubble_sort([])
        self.assertEqual(sorted_collection, [])
