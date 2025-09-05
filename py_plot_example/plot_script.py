import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# 创建图形
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple Plot')
plt.legend()
plt.grid(True)

# 保存图形
plt.savefig('plot.png')
plt.show()