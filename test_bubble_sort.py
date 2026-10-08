import random
import unittest

from bubble_sort import bubble_sort


class _Item:
    """仅按 key 字段参与比较，用于验证排序稳定性。"""

    def __init__(self, key, tag):
        self.key = key
        self.tag = tag

    def __gt__(self, other):
        return self.key > other.key

    def __repr__(self):
        return f"({self.key}, {self.tag})"


class TestBubbleSort(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(bubble_sort([]), [])

    def test_single(self):
        self.assertEqual(bubble_sort([1]), [1])

    def test_already_sorted(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(bubble_sort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_negatives(self):
        self.assertEqual(
            bubble_sort([9, -2, 7, 0, 4, -2, 8, 1]),
            [-2, -2, 0, 1, 4, 7, 8, 9],
        )

    def test_random_large(self):
        random.seed(42)
        nums = [random.randint(-1000, 1000) for _ in range(500)]
        expected = sorted(nums)
        self.assertEqual(bubble_sort(nums), expected)

    def test_in_place_semantics(self):
        nums = [3, 1, 2]
        result = bubble_sort(nums)
        self.assertIs(result, nums)
        self.assertEqual(nums, [1, 2, 3])

    def test_stability(self):
        items = [_Item(1, "a"), _Item(1, "b"), _Item(0, "c"), _Item(1, "d")]
        bubble_sort(items)
        self.assertEqual([item.tag for item in items], ["c", "a", "b", "d"])


if __name__ == "__main__":
    unittest.main()
