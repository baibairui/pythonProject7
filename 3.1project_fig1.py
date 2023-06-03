import matplotlib.pyplot as plt
import numpy as np

#参数
initial_velocity = 10  # 投球初速度 m/s
g = 9.8  # 重力加速度，单位：m/s²
angle_degree = 45
# 把角度转化为弧度
angle_radians = np.radians(angle_degree)
# 计算投球的水平和垂直分量
velocity_x = initial_velocity * np.cos(angle_radians)
velocity_y = initial_velocity * np.sin(angle_radians)
# 计算球到达最高点所需的时间，然后翻倍以得到总飞行时间
total_time = (2 * velocity_y) / g
# 生成时间值
t = np.linspace(0, total_time, num=500)
# 计算每个时间点上球的水平和垂直位置
x = velocity_x * t
y = velocity_y * t - 0.5 * g * t ** 2

# 绘制轨迹
plt.figure(figsize=(10, 5))
plt.plot(x, y, label=f'Angle: {angle_degree} degrees, Initial Velocity: {initial_velocity} m/s')

# 设置图表标题和标签，显示图例
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.title('Basketball Trajectories at Various Angles')
plt.legend()
plt.grid(True)
plt.show()