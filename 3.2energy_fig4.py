import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def caclulate(C_d,A,rho):
    return 0.5*C_d*A*rho

# 参数
C_d = 0.53  # 球体阻力系数
r = 0.123  # 球体半径
A = np.pi * r**2  # 受风面积
rho = 1.293  # 空气密度
m = 1.0  # 质量
g = 9.8  # 重力加速度
H = 1.2  # 初始高度

k = caclulate(C_d,A,rho)  # 空气阻力系数

# 定义微分方程
def dUdt(U, t):
    h, v = U
    dhdt = v
    dvdt = g - k * v**2 / m
    return [dhdt, dvdt]

# 时间数组
t = np.linspace(0, 1, 1000)

# 初始条件
U0 = [0, 0]

# 使用odeint解微分方程
U = odeint(dUdt, U0, t)

# 提取解
h = U[:, 0]
v = U[:, 1]

# 画图
plt.plot(h, v)
plt.xlabel('Height (m)')
plt.ylabel('Velocity (m/s)')
plt.xlim(0,1.5)
plt.grid(True)
plt.show()

