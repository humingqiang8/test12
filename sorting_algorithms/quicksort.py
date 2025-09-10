def quicksort(arr):
    """
    对一个列表进行快速排序。

    参数:
        arr (list): 需要排序的数字列表。

    返回:
        list: 排序后的新列表。
    """
    # 基本情况：如果列表长度小于等于1，则它已经是有序的。
    if len(arr) <= 1:
        return arr
    else:
        # 选择一个基准元素（这里选择中间的元素）。
        pivot = arr[len(arr) // 2]
        # 将列表分割为三个部分：
        # left: 小于基准的元素
        # middle: 等于基准的元素
        # right: 大于基准的元素
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # 递归地对左右两个子列表进行快速排序，然后合并结果。
        return quicksort(left) + middle + quicksort(right)

# 示例用法
if __name__ == "__main__":
    unsorted_list = [3, 6, 8, 10, 1, 2, 1]
    print("原始列表:", unsorted_list)
    sorted_list = quicksort(unsorted_list)
    print("排序后列表:", sorted_list)