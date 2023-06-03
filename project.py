import matplotlib.pyplot as plt
import numpy as np

def project(initvelocity,angle):
    # 设置初始参数
    initial_velocity = initvelocity # 投球初速度 m/s
    g = 9.8  # 重力加速度，单位：m/s²
    angle_degree=angle
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

def angle(initvelocity,angle):
    initial_velocity = initvelocity  # 投球初速度 m/s
    angle_degrees = angle  # 投球角度，单位：度
    g = 9.8  # 重力加速度，单位：m/s²
    mass = 0.62  # 篮球质量，单位：kg
    radius = 0.12  # 篮球半径，单位：m

    # 把角度转化为弧度
    angle_radians = np.radians(angle_degrees)

    # 计算投球的水平和垂直分量
    velocity_x = initial_velocity * np.cos(angle_radians)
    velocity_y = initial_velocity * np.sin(angle_radians)

    # 计算球到达最高点所需的时间，然后翻倍以得到总飞行时间
    total_time = (2 * velocity_y) / g

    # 生成时间值
    t = np.linspace(0, total_time, num=500)

    # 计算初始角动量
    tangential_velocity = initial_velocity
    angular_velocity = tangential_velocity / radius
    moment_of_inertia = 2 / 5 * mass * radius ** 2
    initial_angular_momentum = moment_of_inertia * angular_velocity

    # 由于没有外力矩作用，角动量保持不变
    angular_momentum = initial_angular_momentum * np.ones_like(t)

    # 创建图并绘制角动量变化
    plt.figure()
    plt.plot(t, angular_momentum, label='Angular Momentum')
    plt.xlabel('Time (s)')
    plt.ylabel('Angular Momentum (kg*m²/s)')
    plt.title('Angular Momentum in Basketball Shot')
    plt.legend()
    plt.grid(True)
    plt.show()

def energy(initveloctiy,angle):
    # 设置初始参数
    initial_velocity = initveloctiy # 投球初速度 m/s
    angle_degrees = angle  # 投球角度，单位：度
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

    # 计算每个时间点上球的水平和垂直位置
    x = velocity_x * t
    y = velocity_y * t - 0.5 * g * t ** 2

    # 计算每个时间点上球的动能和势能
    kinetic_energy = 0.5 * mass * (velocity_x ** 2 + (velocity_y - g * t) ** 2)
    potential_energy = mass * g * y
    total_energy = kinetic_energy + potential_energy

    # 创建图并绘制能量变化
    plt.figure()
    plt.plot(t, kinetic_energy, label='Kinetic Energy')
    plt.plot(t, potential_energy, label='Potential Energy')
    plt.plot(t, total_energy, label='Total Energy', linestyle='--')
    plt.xlabel('Time (s)')
    plt.ylabel('Energy (J)')
    plt.title('Energy Change in Basketball Shot')
    plt.legend()
    plt.grid(True)
    plt.show()

def momentum(initvelocity,angle):
    initial_velocity = initvelocity  # 投球初速度 m/s
    angle_degrees = angle# 投球角度，单位：度
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
    velocity_y_t = velocity_y - g*t

    # 计算每个时间点上球的动量
    momentum_x = mass * velocity_x
    momentum_y = mass * velocity_y_t
    total_momentum = np.sqrt(momentum_x**2 + momentum_y**2)

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

def derive(initvelocity,angle):
    # 设置初始参数
    initial_velocity = initvelocity  # 投球初速度 m/s
    g = 9.8  # 重力加速度，单位：m/s²
    angle_degree = angle
    # 把角度转化为弧度
    angle_radians = np.radians(angle_degree)
    # 计算投球的水平和垂直分量
    velocity_x = initial_velocity * np.cos(angle_radians)
    velocity_y = initial_velocity * np.sin(angle_radians)
    # 计算球到达最高点所需的时间，然后翻倍以得到总飞行时间
    total_time = (2 * velocity_y) / g
    # 生成时间值
    t = np.linspace(0, total_time, num=500)
    # 计算投球的水平和垂直分量
    velocity_x = initial_velocity * np.cos(angle_radians)
    velocity_y = initial_velocity * np.sin(angle_radians)

    # 套入公式
    x = velocity_x * t
    y = velocity_y * t - 0.5 * g * t ** 2

    # 计算 y 关于 x 的导数
    dy_dx = np.gradient(y, x)

    # 绘制导数
    plt.figure()
    plt.plot(x, dy_dx,label=f'Angle: {angle_degree} degrees, Initial Velocity: {initial_velocity} m/s')
    plt.title('Derivative of y with respect to x')
    plt.xlabel('x')
    plt.ylabel('dy/dx')
    plt.grid(True)
    plt.show()
