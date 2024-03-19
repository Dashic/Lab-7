#Степанова Дарья R3136 Поток 1.1 Вариант 10
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from matplotlib.animation import PillowWriter
import scipy
import time as time
from random import randint
import csv

#Задание 1
numbers = [randint(1, 1000001) for i in range(1000000)]
numbers1 = [randint(1, 1000001) for z in range(1000000)]
res_list = []
t_list_start = time.perf_counter()
for i in range(0, len(numbers)):
    res_list.append(numbers[i] * numbers1[i])
t_list_stop = time.perf_counter()

num = np.array(numbers, int)
num1 = np.array(numbers1, int)
t_array_start = time.perf_counter()
res = np.multiply(num, num1)
t_array_stop = time.perf_counter()

print(f'Время выполнения поэлементного умножения для numpy меньше чем для стандартных списков на:\
    {(t_list_stop-t_list_start) - (t_array_stop-t_array_start)}')


#Задание 2
sulfate_values = []
with open("data2.csv", encoding='utf-8') as r_file:
    file = list(csv.reader(r_file, delimiter =","))
    file.pop(0)
    for line in file:
        if line[5] != '':
            sulfate_values.append(float(line[5]))
sulfate_values = np.array(sulfate_values, float)


deviation = np.std(sulfate_values)
print(f'Среднеквадратичное отклонение равно {deviation}')

fig = plt.figure(figsize=(10, 4))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
fig.subplots_adjust(wspace=0.5)

ax1.hist(sulfate_values, bins = 20)
ax1.set_title('Распределение')
ax1.set_xlabel('значение измерения')
ax1.set_ylabel('частота')

ax2.hist(sulfate_values, bins = 20, density=True)
ax2.set_title('Нормальное распределение')
ax2.set_xlabel('значение измерения')
ax2.set_ylabel('частота')
plt.show()


#Задание 3
x = np.linspace(-3 * pi, 3 * pi)
y = x * np.cos(x)
z = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('y=xcos(x), z=sin(x)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot(x, y, z, c='violet')
plt.show()

#Доп. задание
LENGTH = 2 * np.pi

animation = PillowWriter(60)
fig = plt.figure()
ax = fig.add_subplot()

animation.setup(fig, 'sin(x).gif')

ax.set_title('График функции y = sin(x)')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')

xs = np.linspace(0, LENGTH, 100)
ys = np.sin(xs)
ax.plot(xs, ys)
dot, = plt.plot([0], [np.sin(0)], 'ro')
animation.grab_frame()

slides = np.linspace(0, LENGTH, 60)
for i in slides:
    dot.set_data(i, np.sin(i))
    animation.grab_frame()

animation.finish()