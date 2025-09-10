def remove_special_characters(input_string, keep_spaces=True):
  """
  过滤字符串中的特殊字符。

  Args:
    input_string: 输入的字符串。
    keep_spaces: 布尔值，如果为True，则保留空格；如果为False，则移除空格。
                    默认值为True。

  Returns:
    过滤后的字符串，只包含字母、数字和（可选的）空格。
  """
  import re
  if keep_spaces:
    # 保留字母、数字和空格
    pattern = r'[^a-zA-Z0-9\s]'
  else:
    # 只保留字母和数字
    pattern = r'[^a-zA-Z0-9]'
  
  cleaned_string = re.sub(pattern, '', input_string)
  return cleaned_string

# --- 示例用法 ---
if __name__ == '__main__':
  test_str = "Hello, World! 123 @#$%^&*()_+-={}[]|\\:;\"'<>?,./"

  # 保留空格
  result_with_spaces = remove_special_characters(test_str, keep_spaces=True)
  print(f"原始字符串: {test_str}")
  print(f"保留空格的结果: '{result_with_spaces}'")

  # 不保留空格
  result_without_spaces = remove_special_characters(test_str, keep_spaces=False)
  print(f"不保留空格的结果: '{result_without_spaces}'")
