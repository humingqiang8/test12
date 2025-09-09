import time
from datetime import datetime

def get_current_time():
    """获取当前时间的字符串表示"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_time(label=""):
    """打印带可选标签的当前时间"""
    current_time = get_current_time()
    if label:
        print(f"[{label}] {current_time}")
    else:
        print(current_time)

# 示例用法
if __name__ == "__main__":
    log_time("开始")
    time.sleep(2) # 模拟一些操作
    log_time("结束")