import numpy as np
import matplotlib.pyplot as plt

initial_velocity = 10 # 投球初速度 m/s
angle_degrees = 45  # 投球角度，单位：度
g = 9.8  # 重力加速度，单位：m/s²
mass = 0.62  # 篮球质量，单位：kg

# 把角度转化为弧度
angle_radians = np.radians(angle_degrees)

# 计算投球的水平和垂直分量
velocity_x = initial_velocity * np.cos(angle_radians)
velocity_y = initial_velocity * np.sin(angle_radians)

# 计算球到达最高点所需的时间，然后翻倍以得到总飞行时间
total_time = (2 * velocity_y) / g

# 生成时间值
t = np.linspace(0, total_time, num=500)

# 计算每个时间点上球的速度（考虑重力）
velocity_y_t = velocity_y - g * t

# 计算每个时间点上球的动量
momentum_x = mass * velocity_x
momentum_y = mass * velocity_y_t
total_momentum = np.sqrt(momentum_x ** 2 + momentum_y ** 2)

# 创建图并绘制动量变化
plt.figure()
plt.plot(t, momentum_x * np.ones_like(t), label='Momentum in x')
plt.plot(t, momentum_y, label='Momentum in y')
plt.plot(t, total_momentum, label='Total Momentum', linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Momentum (kg*m/s)')
plt.title('Momentum Change in Basketball Shot')
plt.legend()
plt.grid(True)
plt.show()