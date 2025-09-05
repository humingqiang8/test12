#!/bin/bash

# 函数: is_number
# 功能: 判断传入的参数是否为一个数字 (整数或浮点数)
# 参数: $1 - 待检测的字符串
# 返回值: 0 (true) 表示是数字, 1 (false) 表示不是数字
# 使用方式: is_number "123.45" && echo "是数字" || echo "不是数字"
is_number() {
    local input="$1"

    # 检查输入是否为空
    if [[ -z "$input" ]]; then
        return 1
    fi

    # 使用正则表达式进行匹配
    # ^[+-]? : 可选的正负号
    # ([0-9]+\.?[0-9]*) : 整数部分和可选的小数部分
    # |(\.[0-9]+) : 或者以小数点开头的小数
    # ([eE][+-]?[0-9]+)? : 可选的科学计数法部分
    if [[ $input =~ ^[+-]?([0-9]+\.?[0-9]*|\.[0-9]+)([eE][+-]?[0-9]+)?$ ]]; then
        return 0
    else
        return 1
    fi
}

# --- 测试用例 ---
echo "Testing is_number function:"
echo "-------------------------"

test_cases=(
    "123"           # 整数
    "-456"          # 负整数
    "123.45"        # 正浮点数
    "+0.123"        # 带正号的浮点数
    ".789"          # 以小数点开头
    "123."          # 以小数点结尾
    "-.456"         # 负小数，以小数点开头
    "1.23e10"       # 科学计数法
    "1.23E-4"       # 大写E的科学计数法
    "+1.23e+5"      # 完整科学计数法
    "abc"           # 非数字字符串
    "123abc"        # 数字与字母混合
    ""              # 空字符串
    "12.34.56"      # 多个小数点
    "12e"           # 不完整的科学计数法
    "inf"           # 无穷大 (本函数不识别为数字)
    "nan"           # 非数字 (本函数不识别为数字)
)

for test_case in "${test_cases[@]}"; do
    if is_number "$test_case"; then
        echo "is_number '$test_case' -> true"
    else
        echo "is_number '$test_case' -> false"
    fi
done