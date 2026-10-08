def bubble_sort(nums):
    """原地升序冒泡排序。

    某一轮未发生任何交换说明已有序，提前退出，
    使已排序输入的复杂度从 O(n^2) 降为 O(n)。
    """
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums


if __name__ == "__main__":
    cases = [
        [],
        [1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 1, 2, 3, 1],
        [9, -2, 7, 0, 4, -2, 8, 1],
    ]
    for case in cases:
        expected = sorted(case)
        assert bubble_sort(case[:]) == expected, f"failed: {case}"
    print("all bubble sort tests passed")
