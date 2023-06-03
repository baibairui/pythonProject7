import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 参数
m = 0.65  # 物体质量
g = 9.8  # 重力加速度
v0 = 10  # 初速度
tho = 53  # 出手角度

C_d = 0.53  # 球体阻力系数
r = 0.123  # 球体半径
A = np.pi * r**2  # 受风面积
rho = 1.293  # 空气密度

def calculate_drag(v):
    """计算给定速度下的阻力大小"""
    return 0.5 * C_d * A * rho * v

def dUdt(U, t):
    """微分方程"""
    x, y, vx, vy = U
    v = np.sqrt(vx**2 + vy**2)
    F_drag = calculate_drag(v)
    dvxdt = -F_drag * vx / (m * v)
    dvydt = -g - F_drag * vy / (m * v)
    dxdt = vx
    dydt = vy
    return [dxdt, dydt, dvxdt, dvydt]

# 初始条件
x0, y0 = 0, 0
vx0 = v0 * np.cos(np.radians(tho))
vy0 = v0 * np.sin(np.radians(tho))
U0 = [x0, y0, vx0, vy0]

# 时间数组
t = np.linspace(0, 1.5, 1000)

# 使用odeint解微分方程（考虑阻力）
U_with_drag = odeint(dUdt, U0, t)

# 无阻力的情况，阻力系数设为0
C_d_no_drag = 0  # 阻力系数为零
def dUdt_no_drag(U, t):
    x, y, vx, vy = U
    dvxdt = 0  # 没有阻力，速度不改变
    dvydt = -g
    dxdt = vx
    dydt = vy
    return [dxdt, dydt, dvxdt, dvydt]

U_no_drag = odeint(dUdt_no_drag, U0, t)

# 提取解
x_with_drag = U_with_drag[:, 0]
y_with_drag = U_with_drag[:, 1]
x_no_drag = U_no_drag[:, 0]
y_no_drag = U_no_drag[:, 1]

plt.plot(x_with_drag, y_with_drag, label='With Drag')
plt.plot(x_no_drag, y_no_drag, label='No Drag')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.legend()
plt.grid(True)
plt.show()

