import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint
from sort_funcs import bubble_sort

# Генерируем случайные данные для сортировки
data = [randint(1, 100) for _ in range(20)]

# Инициализация графика
fig, ax = plt.subplots()
ax.set_title("Bubble Sort Visualization")

# Создаем объект для анимации
bar_rects = ax.bar(range(len(data)), data, align="edge")

# Функция, вызываемая на каждом кадре анимации


def update_fig(data, rects):
    for rect, val in zip(rects, data):
        rect.set_height(val)


# Создаем анимацию
anim = animation.FuncAnimation(
    fig,
    func=update_fig,
    fargs=(bar_rects,),
    frames=bubble_sort(data),
    repeat=False,
    blit=False,
    interval=10,  # Интервал между кадрами в миллисекундах
)

# Показываем график
plt.show()
