def is_number(value):
    """
    判断传入的参数是否为数字
    
    Args:
        value: 任意类型的参数
        
    Returns:
        bool: 如果是数字返回True，否则返回False
    """
    # 处理字符串类型的数字
    if isinstance(value, str):
        # 去除首尾空格
        value = value.strip()
        # 空字符串不是数字
        if not value:
            return False
        # 尝试转换为浮点数
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    # 处理数值类型
    if isinstance(value, (int, float, complex)):
        return True
    
    # 其他类型都不是数字
    return False


# 测试函数
if __name__ == "__main__":
    # 测试用例
    test_cases = [
        123,        # 整数
        3.14,       # 浮点数
        "456",      # 字符串数字
        "7.89",     # 字符串浮点数
        "  123  ",  # 带空格的字符串数字
        "abc",      # 非数字字符串
        "",         # 空字符串
        None,       # None值
        [1, 2, 3],  # 列表
        {"key": "value"}  # 字典
    ]
    
    for case in test_cases:
        result = is_number(case)
        print(f"is_number({repr(case)}) = {result}")