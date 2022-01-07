# 平滑曲线，区别于拟合
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# data
x = np.array([400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2800, 2900, 3000, 4000, 4500, 5000, 5500, 6000, 6500, 7000])  # 最后测试vrms电感
y = np.array([2.57, 2.52, 2.43, 2.30, 2.16, 2.00, 1.87, 1.74, 1.64, 1.53, 1.44, 1.36, 1.29, 1.219, 1.159, 1.103, 1.052, 1.005, 0.961, 0.923, 0.885, 0.852, 0.820, 0.790, 0.763, 0.738, 0.540, 0.481, 0.433, 0.394, 0.361, 0.334, 0.310])

# 这是二次拟合
# f1 = np.polyfit(x, y, 2) # 拟合 非平滑曲线
# ynew = np.polyval(f1, x)

# 这是平滑（过每个点）
list_x_new = np.linspace(min(x), max(x), 1000)
f2 = make_interp_spline(x, y)
list_y_smooth =f2(list_x_new)

plt.plot(list_x_new, list_y_smooth)

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title("标题")
plt.xlabel("f(kHz)")
plt.ylabel("$X_L$(Ω)")
plt.scatter(x, y)

# plt.legend(["charge","discharge"])
plt.grid()
plt.show()