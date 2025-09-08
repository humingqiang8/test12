def bubble_sort(arr):
    """
    冒泡排序算法实现

    Args:
        arr (list): 待排序的整数列表

    Returns:
        list: 排序后的列表
    """
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 最后i个元素已经有序，无需比较
        for j in range(0, n - i - 1):
            # 如果当前元素比下一个元素大，则交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 示例用法
if __name__ == "__main__":
    example_list = [64, 34, 25, 12, 22, 11, 90]
    print("原始列表:", example_list)
    sorted_list = bubble_sort(example_list)
    print("排序后列表:", sorted_list)