import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Параметры броска
v0 = 12.0      # начальная скорость (м/с)
angle = 45.0   # угол броска в градусах
g = 9.81       # ускорение свободного падения

# Расчет физики полета
theta = np.radians(angle)
vx = v0 * np.cos(theta)
vy = v0 * np.sin(theta)

t_flight = (2 * vy) / g
t = np.linspace(0, t_flight, num=100)

x = vx * t
y = vy * t - 0.5 * g * t**2

# Создаем окно графика
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, max(x) * 1.1)
ax.set_ylim(0, max(y) * 1.3)
ax.set_title("Интерактивная симуляция баскетбольного броска")
ax.set_xlabel("Расстояние (м)")
ax.set_ylabel("Высота (м)")
ax.grid(True)
ax.axhline(0, color='black', linewidth=1)

# Линия следа и точка-мяч
line, = ax.plot([], [], '--', color='orange', label="Траектория")
point, = ax.plot([], [], 'o', color='red', markersize=10, label="Мяч")
ax.legend()

# Функция инициализации анимации
def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

# Функция обновления кадров анимации
def animate(i):
    line.set_data(x[:i], y[:i])
    point.set_data([x[i]], [y[i]])
    return line, point

# Запуск анимации
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=len(t), interval=40, blit=True, repeat=True)

plt.show()