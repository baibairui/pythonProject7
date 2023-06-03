import numpy as np
import matplotlib.pyplot as plt

#定义参数
m =0.6 #质量
r =0.123 #半径
v_x =413/300*2**0.5 #水平速度

t = np.linspace(0.05,0.3,10000)
k=(m*r*v_x*(r-(2*(1-r**2))**0.5))/((r**2-1)*t**2)#系数
F = k/t

plt.plot(t,F)
plt.xlabel('Time (s)')
plt.ylabel('F (N)')
plt.grid(True)
plt.show()