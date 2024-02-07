import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint
from sort_funcs import bubble_sort, selection_sort, insertion_sort

matplotlib.rcParams['toolbar'] = 'None'  # removes toolbar from plot

# Генерируем случайные данные для сортировки
data = [randint(1, 100) for _ in range(50)]

# Инициализация графика
fig, ax = plt.subplots()
ax.set_title("Sorts Visualization")
ax.get_xaxis().set_visible(False)  # sets x axis invisible
ax.get_yaxis().set_visible(False)  # sets y axis invisible
# Создаем объект для анимации
bar_rects = ax.bar(range(len(data)), data)

# Функция, вызываемая на каждом кадре анимации

def update_fig(data_color, rects):
    data, color = data_color
    for rect, val, col in zip(rects, data, color):
        rect.set_height(val)
        rect.set_color(col)


# Создаем анимацию
anim = animation.FuncAnimation(
    fig,
    func=update_fig,
    fargs=(bar_rects,),
    frames=insertion_sort(data),
    cache_frame_data=False,
    repeat=False,
    blit=False,
    interval=100,  # Интервал между кадрами в миллисекундах
)

# Показываем график
plt.show()
