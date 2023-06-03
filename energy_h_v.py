import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

def caclulate(C_d,A,rho):
    return 0.5*C_d*A*rho

# 参数
C_d = 0.53#球体阻力系数
r = 0.123#球体半径
A = np.pi * r**2#受风面积
rho = 1.293#空气密度
m = 1.0  # 质量
g = 9.8  # 重力加速度
H = 1.2  # 初始高度

k=caclulate(C_d,A,rho)#空气阻力系数


h=np.linspace(0,1.2,1000)
v=((m*g-g*m*np.exp(-2*k*h))/k)**0.5

plt.plot(h,v)
plt.xlabel('height (m)')
plt.ylabel('velocity (m/s)')
plt.grid(True)
plt.show()