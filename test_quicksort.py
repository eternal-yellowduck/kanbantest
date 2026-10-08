import random
import unittest

from quicksort import quicksort


class _Item:
    """按 key 字段参与全序比较，用于验证当前实现的排序稳定性。

    与 test_bubble_sort._Item（仅定义 __gt__）不同，quicksort 的三路分区
    依赖 <、==、> 三种比较：若只定义 __gt__，同 key 元素会因 == 退化为
    同一性比较而不落入任何分区，被静默丢弃。
    """

    def __init__(self, key, tag):
        self.key = key
        self.tag = tag

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __repr__(self):
        return f"({self.key}, {self.tag})"


class TestQuickSort(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(quicksort([]), [])

    def test_single(self):
        self.assertEqual(quicksort([1]), [1])

    def test_already_sorted(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(quicksort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_negatives(self):
        self.assertEqual(
            quicksort([9, -2, 7, 0, 4, -2, 8, 1]),
            [-2, -2, 0, 1, 4, 7, 8, 9],
        )

    def test_random_large(self):
        random.seed(42)
        nums = [random.randint(-1000, 1000) for _ in range(500)]
        expected = sorted(nums)
        self.assertEqual(quicksort(nums), expected)

    def test_returns_new_list(self):
        nums = [3, 1, 2]
        result = quicksort(nums)
        self.assertIsNot(result, nums)
        self.assertEqual(nums, [3, 1, 2])
        self.assertEqual(result, [1, 2, 3])

    def test_stability(self):
        # 稳定性是当前实现（三路分区、各段保序拼接）的特性，而非通用快排保证。
        items = [_Item(1, "a"), _Item(1, "b"), _Item(0, "c"), _Item(1, "d")]
        result = quicksort(items)
        self.assertEqual([item.tag for item in result], ["c", "a", "b", "d"])
        self.assertEqual([item.tag for item in items], ["a", "b", "c", "d"])


if __name__ == "__main__":
    unittest.main()
