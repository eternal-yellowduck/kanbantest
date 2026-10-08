"""快速排序（返回新列表，不修改调用方数据）"""


def quicksort(arr):
    """对可比较元素列表做升序排序，返回新列表。"""
    if len(arr) <= 1:
        return list(arr)
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quicksort(less) + equal + quicksort(greater)


if __name__ == "__main__":
    cases = [
        [],
        [1],
        [3, 1, 2, 3, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [9, -2, 7, 0, 3, -5, 9],
    ]
    for case in cases:
        print(f"{case} -> {quicksort(case)}")
