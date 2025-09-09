import matplotlib.pyplot as plt
import numpy as np

# 生成数据
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# 创建图表
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine Wave')
plt.legend()
plt.grid(True)

# 保存图表
plt.savefig('sine_wave.png')
plt.show()